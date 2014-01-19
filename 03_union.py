# union procedure for udacity quiz


def union (p1, p2):
    for b in p2:
        if not (b in p1):
            p1.append(b)
    return p1
