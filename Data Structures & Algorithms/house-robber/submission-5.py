class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [-1]*len(nums)
        def recurse(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(nums[i] + recurse(i+2), recurse(i+1))
            return memo[i]

        return recurse(0)
        