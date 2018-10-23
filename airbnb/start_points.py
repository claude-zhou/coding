def startpoints(g):
    def helper(g, v, visited, stk):
        if visited[v]:
            return

        visited[v] = True
        for nei in g[v]:
            helper(g, nei, visited, stk)

        stk.append(v)

    stk = []
    n = len(g)
    visited = [False] * n
    for v in g:
        helper(g, v, visited, stk)

    print(stk)
    visited = [False] * n
    res = []

    for v in stk[::-1]:
        if not visited[v]:
            res.append(v)
            helper(g, v, visited, [])

    return res


# g = {0:[1], 1:[0], 2:[1]}
# assert startpoints(g)==[2]
# g = {0: [2,3], 1:[0], 2:[1], 3:[4], 4:[]}
# assert startpoints(g)==[0]
# g = {0: [2,3], 1:[0], 2:[1], 3:[], 4:[3]}
g = {0: [1, 2], 1: [3, 4], 2: [], 3: [], 4: []}
print(startpoints(g))





