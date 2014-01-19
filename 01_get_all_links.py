# get all links procedure

import urllib2


def get_page(url):
    return urllib2.urlopen(url).read()


def get_next_target(page):
    start_link = page.find('<a href=')

    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def get_all_links(page):
    link_store = []
    while page != None:
        url, endpos = get_next_target(page)
        if url:
            link_store.append(url)
            page = page[endpos:]
        else:
            page = None
    return link_store

links = get_all_links(get_page('http://www.udacity.com/cs101x/index.html'))
print links
