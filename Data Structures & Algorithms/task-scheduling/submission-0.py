class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []
        # need to place the one with the largest number of tasks left
        # per cycle
        for t, c in count.items():
            heapq.heappush(heap, (-c, t))
        cycles = 0
        while len(heap) > 0:
            print(heap)
            curr = []
            maxl = len(heap)
            for _ in range(n+1):
                if len(heap) > 0:
                    c, t = heapq.heappop(heap)
                    if (c + 1) < 0:
                        curr.append((c+1, t))
                cycles += 1
            if len(curr) == 0:
                cycles -= (n+1-maxl)
                return cycles
            for c, t in curr:
                heapq.heappush(heap, (c,t))



        