# 05_hashtable_get_bucket.py


def hash_string(keyword, buckets):
    total = 0
    for letter in keyword:
        total += ord(letter)
    return total % buckets


def hashtable_get_bucket(hashtable, keyword):
    nbuckets = len(hashtable)
    return hashtable[hash_string(keyword, nbuckets)]


table = [[['Francis',  13],  ['Ellis',  11]],
            [],  [['Bill',  17], ['Zoe',  14]],
            [['Coach',  4]], [['Louis',  29],
            ['Rochelle',  4],  ['Nick',  2]]]

print hashtable_get_bucket(table, "Zoe")
#>>> [['Bill', 17], ['Zoe', 14]]

print hashtable_get_bucket(table, "Brick")
#>>> []

print hashtable_get_bucket(table, "Lilith")
#>>> [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]
