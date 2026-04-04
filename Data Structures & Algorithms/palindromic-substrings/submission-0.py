class Solution:
    def countSubstrings(self, s: str) -> int:

        def recurse(left: int, right: int):
            if left < 0 or right >= len(s) or s[left] != s[right]:
                return 0
            else:
                return 1 + recurse(left-1, right+1)

        count = 0
        for i in range(len(s)):
            count += recurse(i, i) + recurse(i, i+1)
        return count
        
        
        
        
        