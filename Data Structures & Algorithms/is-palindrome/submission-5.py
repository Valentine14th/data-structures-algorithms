class Solution:
    def alphanum(self, s: str) -> str:
        out = ""
        s = s.lower()
        for c in s:
            if ord("A") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9"):
                out += c
        return out

    def isPalindrome(self, s: str) -> bool:
        s = self.alphanum(s)
        print(s)
        right = len(s) - 1
        left = 0
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


        