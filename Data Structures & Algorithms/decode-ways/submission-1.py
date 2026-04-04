class Solution:
    def numDecodings(self, s: str) -> int:
        
        def dfs(current, i) -> int:
            if len(current) > 0 and (current[-1][0] == '0' or int(current[-1]) < 1 or int(current[-1]) > 26):
                return 0
            if i == len(s):
                print("correct", current)
                return 1
            # choice: combine or split
            temp = current.copy()
            temp[-1] = temp[-1] + s[i]
            return dfs(current + [s[i]], i+1) + dfs(temp, i+1)

        return dfs([s[0]], 1)
        
        