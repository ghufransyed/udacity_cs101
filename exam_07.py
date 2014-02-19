# find and replace


def make_converter(match, replacement):
    def converter(input):
        if match in input:
            return (input[:input.find(match)] +
                    replacement +
                    input[input.find(match) + len(match):])
        else:
            return input
    return converter


def apply_converter(converter, string):
    if converter(string) == string:
        return string
    else:
        return apply_converter(converter, converter(string))


c1 = make_converter('aa', 'a')
print apply_converter(c1, 'aaaa')
#>>> a
