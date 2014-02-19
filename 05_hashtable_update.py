# 05_hashtable_lookup.py


def hashtable_lookup(htable, key):
    for element in hashtable_get_bucket(htable, key):
        if element[0] == key:
            return element[1]
    else:
        return None


def hashtable_update(htable, key, value):
    if hashtable_lookup(htable, key) is None:
        hashtable_add(htable, key, value)
    else:
        for element in hashtable_get_bucket(htable, key):
            if element[0] == key:
                element[1] = value

#def hashtable_update(htable, key, value):
#    if hashtable_lookup(htable, key) is None:
#        hashtable_add(htable, key, value)
#    else:
#        for element in hashtable_get_bucket(htable, key):
#            if element[0] == key:
#                element.append(value)
#
#    return htable
# both first attempts were wrong due to misunderstanding of specification
# I was adding entries, not updating (changing)


#def hashtable_update(htable, key, value):
#    for element in hashtable_get_bucket(htable, key):
#        if element[0] == key:
#            print "key is %r" % key
#            print "value is %r" % value
#            print "element is %r" % element
#            element.append(value)
#            print "element is %r" % element
#            print "htable is %r" % htable
#            raw_input('Enter any key')
#            return htable
#    else:
#        print "no key found"
#        print "htable is %r" % htable
#        hashtable_add(htable, key, value)
#        print "htable is %r" % htable
#        return htable


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
print table
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


hashtable_update(table, 'Bill', 42)
hashtable_update(table, 'Rochelle', 94)
hashtable_update(table, 'Zed', 68)
hashtable_update(table, 'Blah', 99)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [['Zed', 68]], [['Bill', 42],
#>>> ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Nick', 2],
#>>> ['Rochelle', 94]]]
