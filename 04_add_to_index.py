#add to index


index = []


def add_to_index(index, keyword, url):
    if key_existsp(keyword, index):
        old_keyword(index, keyword, url)
    else:
        new_keyword(index, keyword, url)


def old_keyword(index, keyword, url):
    for i in range(len(index)):
        if index[i][0] == keyword:
            location = i
    index[location][1].append(url)
    return


def key_existsp(key, index):
    flag = False
    for x in index:
        flag = flag or key in x[0]
    return flag


def new_keyword(index, keyword, url):
    index.append([keyword, [url]])
    return


add_to_index(index, 'udacity', 'http://udacity.com')
add_to_index(index, 'computing', 'http://acm.org')
add_to_index(index, 'udacity', 'http://npr.org')
print index
