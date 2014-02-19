#  06_ancestors.py


ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }


def ancestors(genealogy, person):
    result = []
    if person in genealogy:
        for parent in genealogy[person]:
            result.append(parent)
            for element in (ancestors(genealogy, parent)):
                result.append(element)
    return result


print ancestors(ada_family, 'Augusta Ada King')
print ancestors(ada_family, 'Judith Blunt-Lytton')
print ancestors(ada_family, 'Dave')
