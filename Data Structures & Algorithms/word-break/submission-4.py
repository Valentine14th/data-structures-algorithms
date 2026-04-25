class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        dp = [None]*(len(s)+1)
        dp[len(s)] = True
        def rec(i):
            if i == len(s):
                return True
            if dp[i] != None:
                return dp[i]
            for j in range(i, len(s)):
                if s[i:j+1] in wordset:
                    dp[i] = rec(j+1)
                    if dp[i]:
                        return True
            dp[i] = False
            return False
        return rec(0)

        