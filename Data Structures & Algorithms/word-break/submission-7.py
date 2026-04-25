class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [None]*(len(s)+1)
        dp[len(s)] = True
        wordset = set(wordDict)
        maxl = max([len(w) for w in wordDict])
        for i in range(len(s), -1, -1):
            for w in wordDict:
                if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                    if dp[i]:
                        break
        return dp[0] if dp[0] is not None else False


        