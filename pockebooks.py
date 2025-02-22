import csv
from urllib.parse import urlparse
import subprocess
from os.path import exists
import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as infile:
        csv_reader = csv.DictReader(infile)
        unarts = [(row["title"],row["url"]) for row in csv_reader if row["status"] == "unread" and not row["tags"]]
    domains = list(set([urlparse(url).netloc for (_,url) in unarts]))

    for domain in sorted(domains):
        domain_unarts = [unart for unart in unarts if urlparse(unart[1]).netloc == domain]
        filename = domain + ".epub"

        if not exists(filename):
            print(domain)
            print()
            for (n, (title,url)) in enumerate(domain_unarts):
                print(str(n + 1) + ".", title, "({})".format(url))

            title = input("title: ")
            author = input("author: ")
            exclude_string = input("articles to exclude (space-separated): ")
            excludes = [int(n) for n in exclude_string.split(" ")] if exclude_string != "" else []

            selection = []
            for (i,unart) in enumerate(domain_unarts):
                if i + 1 not in excludes:
                    selection.append(unart)

            if title != "" or author != "":
                subprocess.run(["percollate", "epub"] + [url for (_,url) in selection] + ["-o", filename, "-t", title, "-a", author]) 
