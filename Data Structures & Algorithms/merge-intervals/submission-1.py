class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        if len(intervals) == 0:
            return intervals
        res = []
        merge = intervals[0]
        for i in range(1, len(intervals)):
            if merge[1] >= intervals[i][0]:
                merge[1] = max(intervals[i][1], merge[1])
                print(merge)
            else:
                res.append(merge)
                merge = intervals[i]
        res.append(merge)
        return res



        