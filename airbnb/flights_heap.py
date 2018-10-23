from collections import defaultdict
from heapq import *

def findCheapestPrice(n, flights, src, dst, K):
    w = defaultdict(dict)
    for u, v, p in flights:
        w[u][v] = p
    heap = [(0, src, K + 1)]
    # seen = set()
    while heap:
        p, u, K = heappop(heap)
        # seen.add(u)
        if u == dst:
            return p
        if K > 0:
            for v in w[u]:
                # if v not in seen:
                heappush(heap, (p + w[u][v], v, K - 1))
    return -1


print(findCheapestPrice(5, [(0,1,1),(1,2,1),(0,2,6),(2,3,1),(3,4,1)],0,4,2))
