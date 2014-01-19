#check_sudoku

square = [[1, 2, 3],
          [2, 3, 1],
          [3, 1, 2]]


'''
def check_sudoku(square):
    if len(square) == 1:
        return square == 1
    else:
        return (check_row(extract_column(square)) and
                check_row(square[-1]) and
                check_sudoku(extract_square(square)))
 didn't work: I failed to realize that each smaller
 square is not necessarily a sudoku square
so the recursive solution doesn't work (or at least, not as written)
'''


def check_sudoku(square):
    flag = True
    for x in square:
        flag = flag and check_row(x)
    for x in range(len(square)):
        flag = flag and check_row(extract_column(square, x))
    return flag


def extract_column(square, num):
    column = []
    for x in square:
#        print x[0]
#        print x
        column.append(x[num])
    return column

#print extract_column(square)


#def extract_square(square):
#    small_square = []
#    for x in square:
#        small_square.append(x[0:-1])
#    print small_square
#print extract_square(square)


def extract_square(square):
    small_square = []
    length = len(square)
    for x in range(length - 1):
        small_square.append(square[x][0:-1])
    return small_square


def check_row(row):
    flag = True
    for x in range(1, 1 + len(row)):
        flag = flag and x in row
    return flag


print check_sudoku(square)
