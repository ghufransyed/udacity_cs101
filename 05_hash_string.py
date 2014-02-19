# 05_hash_string.py


def hash_string(keyword, buckets):
    total = 0
    for letter in keyword:
        total += ord(letter)
    return total % buckets
