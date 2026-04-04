class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mini = float('inf')
        for sell in range(len(prices)):
            profit = max(profit, prices[sell] - mini)
            mini = min(mini, prices[sell])
        return profit




        