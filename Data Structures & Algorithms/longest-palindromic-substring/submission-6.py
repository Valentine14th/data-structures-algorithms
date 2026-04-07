class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        maxl = 0
        maxis = (0,0)
        dp = [[False]*l for _ in range(l)]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, l):
                if s[i] == s[j] and (j-i+1 <= 2 or dp[i+1][j-1]):
                    if j-i+1 > maxis[1] - maxis[0] + 1:
                        maxis = (i, j)
                    dp[i][j] = True
        return s[maxis[0]:maxis[1]+1]



        