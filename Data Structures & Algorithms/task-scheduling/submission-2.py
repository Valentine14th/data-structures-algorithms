class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxf = max(count.values())
        maxfl = 0
        for c in count.values():
            if c == maxf:
                maxfl += 1
        return max(len(tasks), (maxf-1)*(n+1)+maxfl)

        



        