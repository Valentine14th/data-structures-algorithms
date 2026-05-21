class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float("inf")]*(amount+1) for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 0
        for i in range(1, len(coins)+1):
            for s in range(1, amount+1):
                dp[i][s] = dp[i-1][s]
                if s >= coins[i-1]:
                    dp[i][s] = min(dp[i][s], 1+dp[i][s-coins[i-1]])
        out = dp[len(coins)][amount]
        return out if out != float("inf") else -1

        
            
        