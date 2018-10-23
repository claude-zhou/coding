class Trie:
    def __init__(self):
        self.list = [None] * 26
        self.endpoint = [False] * 26

    def add(self, word):
        idx = ord(word[0]) - ord('a')
        if self.list[idx] is None:
            self.list[idx] = Trie()
        if len(word) == 1:
            self.endpoint[idx] = True
        else:
            self.list[idx].add(word[1:])

    def check(self, word):
        idx = ord(word[0]) - ord('a')
        if self.list[idx] is None:
            return False
        if len(word) == 1:
            return self.endpoint[idx]
        else:
            return self.list[idx].check(word[1:])


directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def findWords(board, words):
    """
    :type board: List[List[str]]
    :type words: List[str]
    :rtype: List[str]
    """
    trie = Trie()
    for word in words:
        assert len(word) != 0
        trie.add(word)

    m = len(board)
    n = len(board[0])

    words = []
    markings = []
    marked = [[False] * n for _ in range(m)]

    def solve(prefix, i, j, t, marked):
        idx = ord(board[i][j]) - ord('a')
        if marked[i][j] or t.list[idx] is None:
            return
        marked[i][j] = True
        new_pre = prefix + board[i][j]
        new_trie = t.list[idx]
        if t.endpoint[idx]:
            words.append(new_pre)
            markings.append([line.copy() for line in marked])
            t.endpoint[idx] = False
        for a, b in directions:
            ii, jj = i + a, j + b
            if 0 <= ii < m and 0 <= jj < n:
                solve(new_pre, ii, jj, new_trie, marked)
        marked[i][j] = False

    def dfs(marked, pos, words):
        if pos == n * m:
            return words
        ii, jj = divmod(pos, n)
        for i in range(ii, m):
            for j in range(jj, n):
                ret = []
                markings = []
                solve('', i, j, trie)

    return ret
