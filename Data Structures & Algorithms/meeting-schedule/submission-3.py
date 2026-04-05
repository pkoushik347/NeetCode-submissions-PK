"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        ln = len(intervals)
        if (ln == 0 or ln == 1):
            return True
        for i in range(ln-1):
            p, n = intervals[i], intervals[i+1]
            if (p.end > n.start):
                return False
        return True