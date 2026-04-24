class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longest(i, j):
            left = i
            right = j
            l = j-i
            while right < len(s) and left >= 0 and s[right] == s[left]:
                left -= 1
                right += 1
                l += 2
            return [left+1, right-1]
        maxi = [0, 0]
        for i in range(len(s)):
            print(maxi)
            l1, r1 = longest(i, i)
            l2, r2 = longest(i, i+1)
            cl, cr = [l1, r1] if (r1-l1) > (r2-l2) else [l2, r2]
            ml, mr = maxi
            maxi = [ml, mr] if (mr-ml) > (cr-cl) else [cl, cr]
        return s[maxi[0]:maxi[1]+1]


        