# 05_hashtable_add.py


def hashtable_add(htable, key, value):
    hashtable_get_bucket(htable, key).append([key, value])
#   return htable
#   this is only needed to pass the udacity auto-checker


def hash_string(keyword, buckets):
    total = 0
    for letter in keyword:
        total += ord(letter)
    return total % buckets


def hashtable_get_bucket(hashtable, keyword):
    nbuckets = len(hashtable)
    return hashtable[hash_string(keyword, nbuckets)]


def make_hashtable(nbuckets):
    table = []
    for unused in range(0, nbuckets):
        table.append([])
        return table


table = make_hashtable(5)
hashtable_add(table, 'Bill', 17)
hashtable_add(table, 'Coach', 4)
hashtable_add(table, 'Ellis', 11)
hashtable_add(table, 'Francis', 13)
hashtable_add(table, 'Louis', 29)
hashtable_add(table, 'Nick', 2)
hashtable_add(table, 'Rochelle', 4)
hashtable_add(table, 'Zoe', 14)
print table

#>>> [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
#>>> [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]
