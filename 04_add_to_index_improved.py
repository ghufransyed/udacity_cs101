#add to index


index = []


def add_to_index(index, keyword, url):
#     print "index is %r" % index
#     print "keyword is %r" % keyword
#     print "url is %r" % url
    for entry in index:
        if entry[0] == keyword:
            for subentry in entry[1]:
                if url == subentry:
                    return
            entry[1].append(url)
            return
    # not found, add new keyword to index
    index.append([keyword, [url]])

add_to_index(index, 'udacity', 'http://udacity.com')
add_to_index(index, 'computing', 'http://acm.org')
add_to_index(index, 'udacity', 'http://npr.org')
print index
