# product_list


def product_list(lst):
    total = 1
    for x in lst:
        total *= x
    return total


#greatest

def greatest(list):
    if list != []:
        return max(list)
    else:
        return 0


# total_enrollment

def total_enrollment(list):
    total_students = 0
    total_tuition = 0

    for x in list:
        total_students += x[1]
        total_tuition += x[1] * x[2]

    return total_students, total_tuition
