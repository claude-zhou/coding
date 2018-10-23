from collections import Counter, deque

def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates = [round(100*c) for c in candidates]
    target = round(100*target)

    c = Counter(candidates)
    uniq_num = list(c.keys())
    uniq_num.sort()
    subsets = deque([[]])
    ret = []
    for n in uniq_num:
        for j in range(len(subsets)):
            flag = False
            s = subsets.popleft()
            summ = sum(s)
            for i in range(1, c[n]+1):
                if n * i + summ < target:
                    n_s = s.copy() + [n] * i
                    subsets.append(n_s)
                    flag = True
                elif n * i + summ == target:
                    n_s = s.copy() + [n] * i
                    ret.append(n_s)
            if flag:
                subsets.append(s)
    return ret

# leetcode 40
