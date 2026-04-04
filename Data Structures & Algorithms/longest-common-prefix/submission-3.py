class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        s1 = strs[0]
        s2 = strs[1]
        longest = 0
        while longest < min(len(s1), len(s2)) and s1[longest] == s2[longest]:
            longest += 1
        print(longest)
        for s in strs[2:]:
            if len(s) < longest:
                longest = len(s)
            while longest > 0 and s[longest-1] != s1[longest-1]:
                longest -= 1
        return s1[:longest] if longest > 0 else ""
         