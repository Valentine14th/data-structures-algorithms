class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        maxi = 0
        for p in prices:
            if p < buy:
                buy = p
            else:
                maxi = max(maxi, p-buy)
        return maxi

        