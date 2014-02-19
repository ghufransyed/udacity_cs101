# exam_08.py


def longest_repetition(lst):
    if not lst:
        return None
    else:
        longest = lst[0]
        current = lst[0]
        counter = 1
        max_num = 1
        for i in range(1, len(lst)):
            if lst[i] == current:
                counter += 1
            else:
                if counter > max_num:
                    max_num = counter
                    longest = current
                current = lst[i]
                counter = 1
        if counter > max_num:
            max_num = counter
            longest = current

        return longest


#  print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
print longest_repetition([2, 2, 3, 3, 3])
