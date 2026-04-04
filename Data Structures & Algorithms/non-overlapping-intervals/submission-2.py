class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        print(intervals)

        end = intervals[0][1]
        remove = 0
        for i in range(1, len(intervals)): 
            # no overlap
            if end <= intervals[i][0]:
                end = intervals[i][1]
            # overlap
            else:
                #remove interval that ends last
                end = min(end, intervals[i][1])
                remove += 1
        return remove
            


        
        