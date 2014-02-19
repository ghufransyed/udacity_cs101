#  exam_09.py


def is_list(p):
    return isinstance(p, list)


def deep_reverse(p):
    result = []
    for i in range(len(p) - 1, -1, -1):
        if is_list(p[i]):
            result.append(deep_reverse(p[i]))
        else:
            result.append(p[i])
    return result


p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse(p)
