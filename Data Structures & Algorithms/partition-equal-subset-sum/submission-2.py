class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        def rec(i, lcurr, rcurr):
            if i >= len(nums):
                return lcurr == rcurr
            fs = frozenset([lcurr, rcurr])
            if fs in memo:
                return memo[fs]
            fl = frozenset([lcurr+nums[i], rcurr])
            fr = frozenset([lcurr, rcurr+nums[i]])
            memo[fl] = rec(i+1, lcurr+nums[i], rcurr)
            memo[fr] = rec(i+1, lcurr, rcurr+nums[i])
            return memo[fl] or memo[fr] 
        
        return rec(0,0,0)


        