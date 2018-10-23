def pourWater(heights, V, K):
    """
    :type heights: List[int]
    :type V: int
    :type K: int
    :rtype: List[int]
    """
    def move(r):
        lowest = heights[K]
        pos = K
        for i in r:
            if heights[i] > lowest:
                return pos
            elif heights[i] < lowest:
                pos = i
                lowest = heights[i]
        return pos

    left = range(K - 1, -1, -1)
    right = range(K + 1, len(heights))
    for i in range(V):
        pos = move(left)
        if pos == K:
            pos = move(right)
        heights[pos] += 1

    return heights


# leetcode #755
