class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        topk = []
        for x, y in points:
            heapq.heappush(topk, (-math.sqrt(x**2+y**2), [x, y]))
            #print(topk)
            if len(topk) > k:
                heapq.heappop(topk)
        return [coor for v, coor in topk]

        