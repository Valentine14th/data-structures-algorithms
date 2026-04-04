class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [-1]*(n+1)
        def rec(curr):
            if curr > n:
                return 0
            if curr == n:
                return 1
            if steps[curr] != -1:
                return steps[curr]
            steps[curr] = rec(curr+1) + rec(curr+2)
            return steps[curr]
        return rec(0)
        