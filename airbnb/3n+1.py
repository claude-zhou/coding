# import sys
# sys.setrecursionlimit(1000)

def p3n_1():
    d = {1:0}

    def get_times(n):
        # print('   ' + str(n))
        if n in d:
            return d[n]
        if n % 2 == 0:
            ret = 1 + get_times(n//2)
        else:
            ret = 1 + get_times(3 * n + 1)
        d[n] = ret
        return ret
    maxx = 0
    for i in range(2, 1000000):
        maxx = max(maxx, get_times(i))
    return maxx


print(p3n_1())
