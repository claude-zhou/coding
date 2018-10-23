from math import floor, ceil

def roundsum(clist):
  print(clist)
  flist = [floor(c) for c in clist]
  print(flist)
  diff = round(sum(clist))-sum(flist)

  dlist = [c-floor(c) for c in clist]
  for n in dlist:
    print("%.1f" % n, end=' ')
  print()
  ret = 0

  dlist.sort(reverse=True)
  for n in dlist:
    print("%.1f" % n, end=' ')
  print('\n')
  for c in dlist:
    if diff > 0:
      diff -= 1
      ret += 1-c
    else:
      ret += c
  return ret


approx_equal = lambda a, b, t: abs(a - b) < t

assert approx_equal(roundsum([1.2, 2.3, 3.4]), 1.1, 0.0001)==True
assert approx_equal(roundsum([1.2, 2.5, 3.6, 4.0]), 1.1, 0.0001)==True
assert approx_equal(roundsum([1.2, 3.7, 2.3, 4.8]), 1.0, 0.0001)==True
assert approx_equal(roundsum([1., 2., 3.]), 0., 0.0001)==True