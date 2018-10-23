# need to be improved

def findCheapestPrice(self, n, flights, src, dst, K):
    """
    :type n: int
    :type flights: List[List[int]]
    :type src: int
    :type dst: int
    :type K: int
    :rtype: int
    """
    fs = {city: dict() for city in range(n)}
    for f in flights:
        if f[1] not in fs[f[0]]:
            fs[f[0]][f[1]] = f[2]
        else:
            fs[f[0]][f[1]] = min(fs[f[0]][f[1]], f[2])
    # for i, j in fs.items():
    #     print(i, j)
    cheapest = {city: float('inf') for city in range(n)}

    cheapest[src] = 0
    now = [src]
    nxt = []
    stop = 0
    while now and stop != K + 1:
        update = []
        for now_city in now:
            for nxt_city, price in fs[now_city].items():
                new_price = cheapest[now_city] + price
                if cheapest[nxt_city] > new_price and cheapest[dst] > new_price:
                    update.append([nxt_city, new_price])
                    nxt.append(nxt_city)
        for city, new_price in update:
            cheapest[city] = min(cheapest[city], new_price)
        stop += 1
        now = nxt
        nxt = []
    if cheapest[dst] == float('inf'):
        return -1
    return cheapest[dst]


n = 10
flights = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
src = 6
dst = 0
K = 7
n = 4
flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
K = 1
print(findCheapestPrice(n, flights, src, dst, K))

# leetcode 787
