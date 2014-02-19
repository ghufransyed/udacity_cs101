###
### webcorpus.py
###

### Define the WebCorpus class here:


class WebCorpus(object):

    def __init__(self):
        self.index = {}
        self.graph = {}

    """
    it turns out that only the above code was needed
    for 09_problemset_03
    """

    def populate(self, p_seed):
        tocrawl = {p_seed}
        crawled = set()
        while tocrawl:
            page = tocrawl.pop()
            if page not in crawled:
                content = get_page(page)
                add_page_to_index(index, page, content)
                outlinks = get_all_links(content)
                graph[page] = outlinks
                tocrawl.update(set(outlinks))
                crawled.update(set(page))
        self.index = index
        self.graph = graph
        # return index, graph


    def get_page(url):
        if url in cache:
            return cache[url]
        else:
            return None

    def get_next_target(page):
        start_link = page.find('<a href=')
        if start_link == -1:
            return None, 0
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote

    def get_all_links(page):
        links = []
        while True:
            url, endpos = get_next_target(page)
            if url:
                links.append(url)
                page = page[endpos:]
            else:
                break
        return links

    def add_page_to_index(index, url, content):
        words = content.split()
        for word in words:
            add_to_index(index, word, url)

    def add_to_index(index, keyword, url):
        if keyword in index:
            index[keyword].append(url)
        else:
            index[keyword] = [url]

    def lookup(index, keyword):
        if keyword in index:
            return index[keyword]
        else:
            return None

    def compute_ranks(graph):
        d = 0.8  # damping factor
        numloops = 10

        ranks = {}
        npages = len(graph)
        for page in graph:
            ranks[page] = 1.0 / npages

        for i in range(0, numloops):
            newranks = {}
            for page in graph:
                newrank = (1 - d) / npages
                for otherpage in graph:
                    if (page in graph[otherpage] and
                        page != otherpage):
                            newrank = (newrank +
                                       d * ranks[otherpage] / len(graph[otherpage]))
                newranks[page] = newrank
            ranks = newranks
        return ranks
