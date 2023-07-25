from bs4 import BeautifulSoup
from urllib.parse import urlparse
import subprocess
from os.path import exists
import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as infile:
        html_str = infile.read()
    soup = BeautifulSoup(html_str, 'html.parser')
    links = soup.find_all('a')
    articles = [link for link in links if link["tags"] == ""]
    domains = list(set([urlparse(article["href"]).netloc for article in articles]))
    misc = []

    for domain in sorted(domains):
        domain_articles = list(reversed([article for article in articles if urlparse(article["href"]).netloc == domain]))
        filename = domain + ".epub"

        if not exists(filename):
            print(domain)
            print()
            for (n, article) in enumerate(domain_articles):
                print(str(n + 1) + ".", article.contents[0])

            title = input("title: ")
            author = input("author: ")
            exclude_string = input("articles to exclude (space-separated): ")
            excludes = [int(n) for n in exclude_string.split(" ")] if exclude_string != "" else []

            selection = []
            for (i,article) in enumerate(domain_articles):
                if i + 1 not in excludes:
                    selection.append(article)


            if title != "" or author != "":
                subprocess.run(["percollate", "epub"] + [article["href"] for article in selection] + ["-o", filename, "-t", title, "-a", author]) 
