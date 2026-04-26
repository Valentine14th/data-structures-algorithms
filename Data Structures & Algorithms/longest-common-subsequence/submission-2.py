class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # we'll have a dp array with 
        # dp[i][j] means the have a common subsequ from i to j
        # but wait no because it might not be in the same place...
        # mm okay, we need to preserve order
        # increasing we checked if common
        # i feel like can use the same ?? but check same?
        # dp[i] mean longest subseq for both starting at i
        # dp = [[-1]*len(text2) for _ in len(text1)]
        # dp[-1][-1] = 1 if text1[-1] == text2[-1] else 0
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        #dp = [0] * (max(len(text1), len(text2)))
        #dp[-1] = 1 if text1[-1] == text2[-1] else 0
        #smaller = text1 if len(text1) < len(text2) else text2
        #bigger = text2 if len(text1) < len(text2) else text1
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    # Characters match: move diagonally and add 1
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    # Characters don't match: take the max of skipping either char
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]


                





        