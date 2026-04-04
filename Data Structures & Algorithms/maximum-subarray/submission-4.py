class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #never start from a negative
        # if at any point reach zero or negative, better to restart
        summ = -float('inf')
        maxx = -float('inf')
        for n in nums:
            summ = max(n, summ+n)
            maxx = max(summ, maxx)
        return maxx


        