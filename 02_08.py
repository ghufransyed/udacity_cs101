def rest_of_string(s):
    return s[1:]


def abbaize(first, second):
    return first + 2 * second + first


print abbaize('a', 'b')


def find_second(search_string, target_string):
    first_position = search_string.find(target_string)
    return search_string.find(target_string, first_position + 1)

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')


twister = "she sells seashells by the seashore"
print find_second(twister, 'she')


word = "madman"
word_length = len(word)

last_letter = word[-1]
first_letter = word[0]

is_palindrome = first_letter.find(last_letter)
print is_palindrome


def biggest(a, b, c):
    if c >= a and c >= b:
        return c
    if a >= b and a >= c:
        return a
    if b >= c and b >= a:
        return b
