class Queue:
    def __init__(self, size=10):
        self.outer = []
        self.inner = self.outer
        self.size = size

    def push(self, ele):
        if len(self.inner) <= self.size-1:
            self.inner.append(ele)
        else:
            self.inner.append([ele])
            self.inner = self.inner[-1]

    def pop(self):
        if len(self.outer) > 1:
            ret = self.outer[0]
            self.outer = self.outer[1:]
            return ret
        elif len(self.outer) == 1:
            if isinstance(self.outer[0], list):
                self.outer = self.outer[0]
                return self.pop()
            else:
                return self.outer.pop()
        else:
            return None


q = Queue(5)

for i in range(10):
    q.push(i)
    print(q.outer)
for i in range(5):
    print(q.pop())
    print(q.outer)
for i in range(10, 20):
    q.push(i)
    print(q.outer)
for i in range(10):
    print(q.pop())
    print(q.outer)
