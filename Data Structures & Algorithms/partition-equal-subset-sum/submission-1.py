class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        def rec(i, lcurr, rcurr):
            if i >= len(nums):
                return lcurr == rcurr
            if frozenset([lcurr, rcurr]) in memo:
                return memo[frozenset([lcurr, rcurr])]
            memo[frozenset([lcurr+nums[i], rcurr])] = rec(i+1, lcurr+nums[i], rcurr)
            memo[frozenset([lcurr, rcurr+nums[i]])] = rec(i+1, lcurr, rcurr+nums[i])
            return memo[frozenset([lcurr+nums[i], rcurr])] or memo[frozenset([lcurr, rcurr+nums[i]])] 
        
        return rec(0,0,0)


        