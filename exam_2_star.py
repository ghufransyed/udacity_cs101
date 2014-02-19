# exam_2_star.py
# link_spam


g = {'a': ['a', 'b', 'c'], 'b': ['a'], 'c': ['d'], 'd': ['a']}


def lookup_link(graph, link_start, link_target, depth):
    if link_start in graph[link_start]:
        return True
    elif depth == 0:
        return False
    elif link_start in graph[link_target]:
        return True
    elif depth == 1:
        return False
    result = False
    if depth >= 2:
        for node in graph[link_target]:
            result = (result or
                      lookup_link(graph, link_start, node, depth - 1))
    return result

# for start in ['a', 'b', 'c']:
#     for end in ['a', 'b', 'c']:
#         for n in range(4):
#             print "link from %r to %r in %r steps?: %r" % (
#                 start, end, n, lookup_link(g, start, end, n))
