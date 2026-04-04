class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        robs = [-1]*(n+1)
        def rec(i):
            if i >= n:
                return 0
            if robs[i] != -1:
                return robs[i]
            robs[i] = max(rec(i+2) + nums[i], rec(i+1))
            return robs[i]
        return rec(0)

        