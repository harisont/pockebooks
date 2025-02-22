# Pockebooks

A simple Python script to build ebooks from a [Pocket](https://getpocket.com) list of unread articles.

## Is Pockebooks for you?
No, it is for me. 
In fact, it builds ebooks [in a very specific way](#what-does-pockebooks-do-exactly) which probably doesn't suit your needs.
With that being said, you are welcome to use and customize it. 

## Dependencies
- External: [percollate](https://github.com/danburzo/percollate)
- Python: you'll figure it out

## Usage
```
python pockebooks.py EXPORTED_SAVES.html
```

## What does Pockebooks do exactly? 
Pockebooks is a simple Python script to build ebooks (in `.epub` format) from __[the CSV export](https://getpocket.com/export)__ of your [Pocket](https://getpocket.com) saves.

It selects __untagged unread articles__ and groups them by __web domain__. 
For each domain, it allows to interactively create an ebook with [percollate](https://github.com/danburzo/percollate). 
To create an ebook, the user __*must* choose a title *and* an author__ (if either is left empty, the ebook is not created) and __*can* select a set of articles to ignore__. 

Files are __created in the working directory__ and __named as the source domain__.
__If a file with a certain domain name already exists, it will *not* be overwritten__.  

## Some other questions that nobody asked

### Why don't you use the Pocket API?
I don't know, that was the idea, but the access token doesn't work or something like that.

### Why don't you generate the ebooks with a Python library instead of using percollate?
Because [percollate](https://github.com/danburzo/percollate) generates amazing ebooks with no effort from my side.

### Why untagged articles specifically?
Because not tagging is my lazy way to say that the article I'm saving is mostly text and can probably be enjoyed on an e-reader. 

### Why do I _have_ to write a title and an author?
Beacuse Pocket sucks to extract metadata and [I care about basic ebook metadata a lot](https://github.com/harisont/me-tadah).

### Why does Pockebooks not overwrite existing ebooks?
Because my "to read" list tends to get very long and I want to be able to generate the ebooks little by little.

### Will this be further developed into a somewhat decent program?
Probably not, honestly the plan is to abandon Pocket as soon as I read everything and replace it with something open source.