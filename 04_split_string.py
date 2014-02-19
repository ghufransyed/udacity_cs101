# split_string (lesson 4 problem set)


def split_string(source, splitlist):
    result = []
    word = ""
    for letter in source:
        if letter not in splitlist:
            word = word + letter
        else:
            if word:
                result.append(word)
                word = ""
    if word:
        result.append(word)
    return result


# out = split_string("This is a test-of the,string separation-code!"," ,!-")
# print out
#
# out = split_string("After  the flood   ...  all the colors came out.", " .")
# print out
#
# out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
# print out
