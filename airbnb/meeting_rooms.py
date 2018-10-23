def meetingrooms(intervals, start, end):
    intervals.sort(key=lambda x: x[0])
    ret = []
    for it in intervals:
        if end <= it[0]:
            break
        if start < it[0]:
            ret.append((start, it[0]))
        start = max(start, it[1])
        if end <= it[1]:
            break

    if start < end:
        ret.append((start, end))

    return ret


assert meetingrooms([[1, 6], [2, 5], [7, 8]], 5, 7) == [(6, 7)]  # overlapping as well as new
assert meetingrooms([[2, 3], [5, 6], [8, 9]], 0, 10) == [(0, 2), (3, 5), (6, 8), (9, 10)]  # cover all
assert meetingrooms([[2, 6], [8, 9]], 2, 3) == []  # no free room
assert meetingrooms([[2, 7], [3, 8]], 8, 8) == []  # no free room
assert meetingrooms([[2, 7], [3, 8]], 0, 8) == [(0, 2)]  # free at beginning
