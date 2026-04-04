class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        out = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            out.append(intervals[i])
            i+=1
        if i == len(intervals):
            return out + [newInterval]
        if intervals[i][0] > newInterval[1]:
            return out + [newInterval] + intervals[i:]
        l = min(newInterval[0], intervals[i][0])
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            i += 1
        r = max(newInterval[1], intervals[i-1][1])
        return out + [[l, r]] + intervals[i:]
        
        
        
        