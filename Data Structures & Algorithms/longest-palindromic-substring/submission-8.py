class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*len(s) for _ in range(len(s))]
        maxlen = [0,0]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    maxlen = maxlen if maxlen[1]-maxlen[0] > j-i else [i, j]
        return s[maxlen[0]:maxlen[1]+1]
        