class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        maxi = float("-inf")

        for n in nums:
            curr = max(curr + n, n)
            maxi = max(curr, maxi)

        return maxi


        
        