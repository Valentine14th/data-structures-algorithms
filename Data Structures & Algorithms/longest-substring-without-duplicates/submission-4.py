class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        left = 0
        right = 0
        longest = 0
        while right < len(s):
            print(left, right)
            if s[right] in chars:
                bound = chars[s[right]]
                while left <= bound:
                    print("del", right, s[left], chars[s[left]])
                    del chars[s[left]]
                    left += 1
            else:
                longest = max(longest, right-left+1)
            chars[s[right]] = right
            right += 1
        return longest
            

        