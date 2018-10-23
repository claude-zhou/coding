class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def employeeFreeTime(schedule):
    """
    :type schedule: List[List[Interval]]
    :rtype: List[Interval]
    """
    ret = []
    timespots = []
    for intervals in schedule:
        for i in intervals:
            timespots += [(i.start, 0), (i.end, 1)]
    timespots.sort()
    start = None
    num_busy = 0
    for time, typ in timespots:
        if typ == 0:
            if num_busy == 0 and start is not None:
                ret.append(Interval(start, time))
            num_busy += 1
        else:
            num_busy -= 1
            if num_busy == 0:
                start = time
    return ret

def employeeFreeTime_2(schedule):
    start = float('-inf')
    intervals = [i for interval in schedule for i in interval]
    intervals.sort(key=lambda x: x.start)
    ret = []
    for it in intervals:
        if start != float('-inf') and start < it.start:
            ret.append(Interval(start, it.start))
        start = max(start, it.end)
    return ret

# leetcode 759
