from collections import defaultdict, Counter

class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = defaultdict(set)
        c = Counter()
        for w in words:
            for l in w:
                c[l] = 0
                graph[l] = set()

        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        c[w2[j]] += 1
                    break
        ret = ''
        while c:
            flag = False
            to_del = []
            for l in c:
                if c[l] == 0:
                    flag = True
                    to_disconnect = graph.pop(l)
                    for m in to_disconnect:
                        c[m] -= 1
                    ret += l
                    to_del.append(l)
            if not flag:
                return ''
            for l in to_del:
                c.pop(l)
        return ret


s = Solution()
print(s.alienOrder(["wrt","wrf","er","ett","rftt","te"]))