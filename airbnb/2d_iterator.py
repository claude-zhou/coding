class TwoDIterator:
    def __init__(self, clist):
        self.vec = clist
        self.i = 0
        self.j = 0

    def hasNext(self):
        m = len(self.vec)
        while self.i < m and self.j == len(self.vec[self.i]):
            self.i += 1
            self.j = 0
        return self.i < m

    def next(self):
        if not self.hasNext():
            return None
        ret = self.vec[self.i][self.j]
        self.j += 1
        self.hasNext()
        return ret

    def remove(self):
        # get_last
        while self.i > 0 and self.j == 0:
            self.i -= 1
            self.j = len(self.vec[self.i])
        if self.j == 0:
            return
        self.j -= 1
        self.vec[self.i].pop(self.j)
        self.hasNext()


clist = [[1,2,3], [4], [5]]
ti = TwoDIterator(clist)
while ti.hasNext():
  ret = ti.next()
  print(ret)
  if ret==3 or ret==4:
    ti.remove()
    print(clist)
    ti.remove()
    print(clist)
    print()

ti.remove()
print(clist)
ti.remove()
print(clist)
ti.remove()
print(clist)
