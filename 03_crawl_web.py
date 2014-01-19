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


def crawl_web(url):
    crawled = []
    to_crawl = get_all_links(get_page(url))

    #process each link in to_crawl (if not already crawled)
    while to_crawl:
        for s in to_crawl:
            if s in crawled:
                to_crawl.remove(s)
            else:
                for x in get_all_links(get_page(s)):
                    to_crawl.append(x)
                crawled.append(s)
        return crawled

for x in crawl_web('http://www.udacity.com/cs101x/index.html'):
    print x
