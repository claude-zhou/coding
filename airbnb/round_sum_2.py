import math

def roundPricesToMatchTarget(prices, target):
    flist = [math.floor(c) for c in prices]
    diff = target - sum(flist)

    ilist = list(range(len(prices)))
    ilist.sort(key=lambda i: prices[i] - flist[i], reverse=True)
    for i in ilist:
        if diff > 0:
            diff -= 1
            flist[i] += 1
        else:
            break
    return flist


print(roundPricesToMatchTarget([.7, 2.8, 4.9], 8))
