class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pal(i, j):
            if i >= 0 and j < len(s) and s[i] == s[j]:
                return pal(i-1, j+1)
            return (i+1, j-1)
        maxi = (0,0)
        for i in range(len(s)):
            l, r = pal(i,i)
            l1, r1 = pal(i, i+1)
            l, r = (l, r) if r-l+1 > r1-l1+1 else (l1, r1)
            maxi = maxi if maxi[1] - maxi[0] + 1 > r-l+1 else (l, r) 
        return s[maxi[0]:maxi[1]+1]


        