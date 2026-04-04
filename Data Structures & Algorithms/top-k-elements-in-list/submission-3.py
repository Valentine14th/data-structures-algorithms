class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        for n, f in freq.items():
                heapq.heappush(heap, (f, n))
                if len(heap) > k:
                    heapq.heappop(heap)
        return [n for f ,n in heap]




        