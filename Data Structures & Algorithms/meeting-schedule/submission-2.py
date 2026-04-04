"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort by start time
        intervals.sort(key=lambda x: x.start)
        # if any overlap between end and start then not possible
        for i in range(len(intervals)-1):
            print(i)
            if intervals[i].end > intervals[i+1].start:
                return False
        return True
