"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # if overlap, need 2 separate rooms
        # but if overlap with two end, then only 2 is okay, no need 3
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: x.start)
        rooms = [] # heap
        heapq.heappush(rooms, intervals[0].end)
        for inter in intervals[1:]:
            # if no overlap
            if inter.start >= rooms[0]:
                # then remove the earliest room
                heapq.heappop(rooms)
            # push replaced room or new room
            heapq.heappush(rooms, inter.end)
        return len(rooms)


        