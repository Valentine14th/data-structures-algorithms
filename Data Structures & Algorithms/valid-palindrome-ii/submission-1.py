class Solution:
    def validPalindrome(self, s: str) -> bool:
        delete = False
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                skipL = s[left+1:right+1]
                skipR = s[left:right]
                return skipR == skipR[::-1] or skipL == skipL[::-1]
            else:
                right -= 1
                left += 1
        return True
                    

        