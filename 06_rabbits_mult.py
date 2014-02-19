# rabbits multiplying (hw problem)


def rabbits(n):
    result = []
    if n == 1:
        result = [1]
    elif n == 2:
        result = [1, 1]
    else:
        result = [1, 1]
        for i in range(3, n + 1):
            if i <= 5:
                result.append(result[-2] + result[-1])
            else:
                result.append(result[-2] +
                              result[-1] -
                              result[-5])
    return result[-1]


print rabbits(10)
#>>> 35

s = ""
for i in range(1, 12):
    s = s + str(rabbits(i)) + " "
print s
#>>> 1 1 2 3 5 7 11 16 24 35 52
#
# original version (fibonacci)
#def rabbits(n):
#    result = []
#    if n == 1:
#        result = [1]
#    elif n == 2:
#        result = [1, 1]
#    else:
#        result = [1, 1]
#        for i in range(3, n + 1):
#            result.append(result[-2] + result[-1])
#    return result[-1]
