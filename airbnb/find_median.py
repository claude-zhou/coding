import sys

def find_median(num_list):
    length = len(num_list)

    b, e = -sys.maxsize, sys.maxsize

    while True:
        m = (b + e) // 2
        gr, eq = 0, 0
        for num in num_list:
            if num > m:
                gr += 1
            elif num == m:
                eq += 1

        if gr + eq > length / 2 > gr:
            return m
        if gr + eq == length / 2:
            upper = m
            break
        elif gr + eq < length / 2:
            e = m - 1
        else:
            b = m + 1

    e = upper - 1
    while True:
        m = (b + e) // 2
        ls, eq = 0, 0
        for num in num_list:
            if num < m:
                ls += 1
            elif num == m:
                eq += 1

        if eq > 0 and ls + eq == length / 2:
            return (upper + m) / 2
        elif eq == 0 and ls + eq == length / 2:
            e = m - 1
        elif ls + eq != length / 2:
            b = m + 1


print(find_median([1,2,2,2,2]))
