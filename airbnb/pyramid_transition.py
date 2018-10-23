def pyramidTransition(bottom, allowed):
    """
    :type bottom: str
    :type allowed: List[str]
    :rtype: bool
    """

    triples = {t[:2]: [] for t in allowed}
    for t in allowed:
        triples[t[:2]].append(t[2])

    def dfs(bottom, top, pos):
        if len(bottom) == 1:
            return True
        if bottom[pos:pos + 2] not in triples:
            return False
        elif pos == len(bottom) - 2:
            for block in triples[bottom[pos:pos + 2]]:
                if dfs(top + block, '', 0):
                    return True
            return False
        else:
            for block in triples[bottom[pos:pos + 2]]:
                if dfs(bottom, top + block, pos + 1):
                    return True
            return False

    return dfs(bottom, '', 0)

# lc756
