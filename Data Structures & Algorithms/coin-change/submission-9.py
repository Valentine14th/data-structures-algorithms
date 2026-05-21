class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float("inf")]*(amount+1) for _ in range(len(coins))]
        def rec(i, s):
            if s == 0:
                return 0
            if i >= len(coins) or s < 0:
                return float("inf")
            if dp[i][s] != float("inf"):
                return dp[i][s]
            dp[i][s] = min(1 + rec(i, s-coins[i]), rec(i+1, s))
            return dp[i][s]
        out = rec(0, amount)
        return out if out != float("inf") else -1
            
        