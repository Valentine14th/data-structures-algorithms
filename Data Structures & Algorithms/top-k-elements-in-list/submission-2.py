class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        for n, f in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (f, n))
            else:
                if f >= heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (f, n))
        return [n for f ,n in heap]




        