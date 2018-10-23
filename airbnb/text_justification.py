def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    groups = [[]]
    lengths = []
    now_len = 0
    for w in words:
        if now_len + len(w) + 1 <= maxWidth + 1:
            now_len += len(w) + 1
            groups[-1].append(w)
        else:
            lengths.append(now_len-len(groups[-1]))
            now_len = len(w) + 1
            groups.append([w])
    lengths.append(now_len-len(groups[-1]))
    ret = []
    for i, group in enumerate(groups):
        if len(group) == 1 or i == len(groups)-1:
            line = ' '.join(group)
            ret.append(line + ' ' * (maxWidth - len(line)))
            continue
        interval = (maxWidth - lengths[i]) // (len(group) - 1)
        num = maxWidth - lengths[i] - interval * (len(group) - 1)
        for j in range(num):
            group[j] += ' '
        ret.append((' '*interval).join(group))
    return ret

# leetcode 68