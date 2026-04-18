class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def rec(current, i):
            if current == amount:
                return 0
            take = float("inf")
            next = float("inf")
            if (current, i) in memo:
                return memo[(current, i)]
            if current+coins[i] <= amount:
                take = 1 + rec(current+coins[i], i)
            if i+1 < len(coins):
                next = rec(current, i+1)
            memo[(current, i)] = min(take, next)
            return memo[(current, i)]
        out = rec(0,0)
        return out if out != float("inf") else -1



        