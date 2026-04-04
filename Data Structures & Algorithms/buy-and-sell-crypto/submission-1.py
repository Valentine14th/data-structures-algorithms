class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 0
        maxProfit = 0
        left = 0
        right = 1
        while right < len(prices) and left < len(prices):
            currentProfit = prices[right] - prices[left]
            if prices[right] < prices[left]:
                left = right
                right = left + 1
            else:
                right += 1
                if currentProfit > maxProfit:
                    maxProfit = currentProfit
        return maxProfit
                

        