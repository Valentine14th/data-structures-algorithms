class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minP = 1
        maxP = 1
        currP = float("-inf")
        for n in nums:
            temp = minP
            minP = min(n, n*minP, n*maxP)
            maxP = max(n, n*maxP, n*temp)
            currP = max(currP, minP, maxP)
        return currP