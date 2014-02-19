# deep_count.py


def is_list(p):
    return isinstance(p, list)


def deep_count(p):
    total = 0
    for element in p:
        if is_list(element):
            if element == []:
                total += 1
            else:
                total = (total +
                         1 +
                         deep_count(element))
        else:
            total += 1
    return total
