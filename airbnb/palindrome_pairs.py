# need to be improved

# def is_palim(s):
#     for i in range(len(s) // 2):
#         if s[i] != s[-1 - i]:
#             return False
#     return True
#
# def palindromePairs(words):
#     """
#     :type words: List[str]
#     :rtype: List[List[int]]
#     """
#     s2i = dict()
#     for i, s in enumerate(words):
#         s2i[s] = i
#
#     ret = []
#     for ind, s in enumerate(words):
#         new_s = ''
#         if new_s in s2i and s != new_s and is_palim(s):
#             ret.append([ind, s2i[new_s]])
#         for i in range(len(s)):
#             new_s = s[i] + new_s
#             if new_s in s2i and ind != s2i[new_s] and is_palim(s[i + 1:]):
#                 ret.append([ind, s2i[new_s]])
#
#         new_s = ''
#         if new_s in s2i and ind != s2i[new_s] and is_palim(s):
#             ret.append([s2i[new_s], ind])
#         for i in range(len(s) - 1):
#             new_s += s[-1 - i]
#             if new_s in s2i and ind != s2i[new_s] and is_palim(s[:len(s) - i - 1]):
#                 ret.append([s2i[new_s], ind])
#
#     return ret

def palindromePairs(words):
    ret = []
    w2i = {word: i for i, word in enumerate(words)}
    for i, w in enumerate(words):
        for j in range(len(w)+1):
            prefix = w[0:j]
            suffix = w[j:]
            fixpre = prefix[::-1]
            fixsuf = suffix[::-1]
            if j != 0 and prefix == fixpre and fixsuf in w2i and w2i[fixsuf] != i:
                ret.append((w2i[fixsuf], i))
            if suffix == fixsuf and fixpre in w2i and w2i[fixpre] != i:
                ret.append((i, w2i[fixpre]))
    return ret


print(palindromePairs(["abcd","dcba","lls","s","sssll"]))
# leetcode 336
