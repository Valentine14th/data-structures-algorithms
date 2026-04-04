class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * x for x in stones]
        print(heap)
        heapq.heapify(heap)
        while len(heap) > 1:
            print(heap)
            one = heapq.heappop(heap)
            two = heapq.heappop(heap)
            if one != two:
                heapq.heappush(heap, -abs(one-two))
        return - heap[0] if len(heap) != 0 else 0


        
        