# q4 remove tags


def remove_tags(string):
    result = []
    tag_start = string.find('<')
    tag_end = string.find('>', tag_start + 1)

    if tag_start == -1:
        for word in string.split():
            result.append(word)
        return result
    else:
        for word in string[:tag_start].split():
            result.append(word)
        result += remove_tags(string[tag_end + 1:])
    return result

# print remove_tags('''<h1>Title</h1><p>This is a
#                    <a href="http://www.udacity.com">link</a>.<p>''')

print remove_tags("This is plain text.")
