from heapq import *

def wizarddist(g, target):
    q = [(0,0)] # cost, node id
    seen = set()
    while q:
        cost, v = heappop(q)
        if v in seen:
            continue
        if v==target:
            return cost
        seen.add(v)
        for nei in g.get(v, ()):
            if nei not in seen:
                c = (v-nei)*(v-nei)
                heappush(q, (cost+c, nei))
    return float("inf")
