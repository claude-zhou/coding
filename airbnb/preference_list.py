# def preferenceList(plist):
#     # graph
#     elements = set([c for p in plist for c in p])
#     g = {w: list() for w in elements}
#     for p in plist:
#         for i in range(1, len(p)):
#             g[p[i - 1]].append(p[i])
#
#     def dfs(e, visited, recStk):
#         if e in visited:
#             return
#
#         visited.add(e)
#         for nei in g[e]:
#             dfs(nei, visited, recStk)
#
#         recStk.append(e)
#
#     stk = []
#     visited = set()
#     for e in elements:
#         dfs(e, visited, stk)
#
#     return stk[::-1]

# def preferenceList(plist):
#     elements = set([c for p in plist for c in p])
#     connection = {w: [] for w in elements}
#     degree = {w: 0 for w in elements}
#     for p in plist:
#         for i in range(1, len(p)):
#             connection[p[i-1]].append(p[i])
#             degree[p[i]] += 1
#
#     ret = []
#     while connection:
#         to_remove = 0
#         for k, v in degree.items():
#             if v == 0:
#                 to_remove = k
#                 break
#         for n in connection[to_remove]:
#             degree[n] -= 1
#         degree.pop(to_remove)
#         connection.pop(to_remove)
#         ret.append(to_remove)
#
#     return ret

def preferenceList(plist):
    elements = set([c for p in plist for c in p])
    graph = {w: set() for w in elements}
    degree = {w: 0 for w in elements}
    for p in plist:
        for i in range(1, len(p)):
            n1, n2 = p[i-1], p[i]
            if n2 not in graph[n1]:
                graph[n1].add(n2)
                degree[n2] += 1

    ret = []
    while degree:
        flag = False
        to_remove = []
        for k, v in degree.items():
            if v == 0:
                to_remove.append(k)
                flag = True
                ret.append(k)
                for n in graph[k]:
                    degree[n] -= 1
        if not flag:
            return None
        for n in to_remove:
            degree.pop(n)
            graph.pop(n)
    return ret

print(preferenceList([[3, 5, 7, 9],[2, 3, 8],[5, 8]]))