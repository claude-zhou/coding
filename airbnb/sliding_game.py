def serialize(board):
    ret = ''
    for line in board:
        ret += ''.join([str(n) for n in line])
    return ret


def slidingPuzzle(board):
    """
    :type board: List[List[int]]
    :rtype: int
    """
    final_state = [[1, 2, 3], [4, 5, 0]]
    if final_state == board:
        return 0

    for i in range(len(board)):
        if 0 in board[i]:
            j = board[i].index(0)
            break
    visited = {serialize(board)}
    now = [[board, i, j]]
    nxt = []
    update = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    step = 0
    while now:
        step += 1
        for now_b, i, j in now:
            for a, b in update:
                ii, jj = i + a, j + b
                if 0 <= ii < 2 and 0 <= jj < 3:
                    new_b = [line.copy() for line in now_b]
                    new_b[i][j], new_b[ii][jj] = new_b[ii][jj], new_b[i][j]
                    if new_b == final_state:
                        return step
                    serial = serialize(new_b)
                    if serial not in visited:
                        visited.add(serial)
                        nxt.append([new_b, ii, jj])
        now = nxt
        nxt = []

    return -1

# leetcode 773. Sliding Puzzle
