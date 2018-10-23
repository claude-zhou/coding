# need to check on the description of the airbnb boggle game

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

    ret = []
    marked = [[False] * n for _ in range(m)]

    def solve(prefix, i, j, t):
        idx = ord(board[i][j]) - ord('a')
        if marked[i][j] or t.list[idx] is None:
            return
        marked[i][j] = True
        new_pre = prefix + board[i][j]
        new_trie = t.list[idx]
        if t.endpoint[idx]:
            ret.append(new_pre)
            t.endpoint[idx] = False
        for a, b in directions:
            ii, jj = i + a, j + b
            if 0 <= ii < m and 0 <= jj < n:
                solve(new_pre, ii, jj, new_trie)
        marked[i][j] = False

    for i in range(m):
        for j in range(n):
            solve('', i, j, trie)
    return ret

# leetcode 212
