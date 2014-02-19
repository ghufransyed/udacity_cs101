###
### search.py
###
### Modify the lucky_search and ordered_search functions here
### so that they do not take a ranks parameter, but instead use the ranks in the WebCorpus object


def lookup(windex, keyword):
    if keyword in windex.index:
        return windex.index[keyword]
    else:
        return None

# Modify this to take WebCorpus object


def lucky_search(wcorpus, keyword):
    pages = wcorpus.lookup(keyword)
    if not pages:
        return None
    best_page = pages[0]
    for candidate in pages:
        if wcorpus.page_rank(candidate) > wcorpus.page_rank(best_page):
                best_page = candidate
    return best_page


def quicksort_pages(pages, wcorpus):
    if not pages or len(pages) <= 1:
        return pages
    else:
        pivot = wcorpus.page_rank(pages[0])
        worse = []
        better = []
        for page in pages[1:]:
            if wcorpus.page_rank(page) <= pivot:
                worse.append(page)
            else:
                better.append(page)
        return quicksort_pages(better, wcorpus) + [pages[0]] + quicksort_pages(worse, wcorpus)


# Modify this to take WebCorpus object

def ordered_search(wcorpus, keyword):
    pages = wcorpus.lookup(keyword)
    return quicksort_pages(pages, wcorpus)
