class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None]*(amount+1)
        def rec(s):
            if s == amount:
                return 0
            if s > amount:
                return float("inf")
            if dp[s] != None:
                return dp[s]
            for c in coins:
                dp[s] = min(1+rec(s+c), dp[s] if dp[s] is not None else float("inf"))
            return dp[s]
        t = rec(0)
        return t if t != float("inf") else -1
        