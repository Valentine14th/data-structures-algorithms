class MedianFinder:
    # as many bigger and as many smaller
    # keep heap of k largest and k smallest

    def __init__(self):
        self.minh = []
        self.maxh = []

    def addNum(self, num: int) -> None:
        # keep heaps balanced
        if len(self.minh) == 0 or num > self.minh[0]:
            heapq.heappush(self.minh, num)
        else:
            heapq.heappush(self.maxh, -num)
        if abs(len(self.minh) - len(self.maxh)) > 1:
            if len(self.minh) > len(self.maxh):
                m = heapq.heappop(self.minh)
                heapq.heappush(self.maxh, -m)
            else:
                m = heapq.heappop(self.maxh)
                heapq.heappush(self.minh, -m)

    def findMedian(self) -> float:
        if len(self.minh) == 0 and len(self.maxh) == 0:
            return 0
        if len(self.minh) == len(self.maxh):
            return (self.minh[0]+(-self.maxh[0])) / 2
        if len(self.maxh) > len(self.minh):
            return -self.maxh[0]
        else:
            return self.minh[0]
    
        
        