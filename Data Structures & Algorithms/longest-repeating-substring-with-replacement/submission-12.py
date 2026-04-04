class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        counts = {}
        left = 0
        right = 0
        maxchar = s[0]
        maxlen = 0
        while right < len(s):
            counts[s[right]] = counts.get(s[right], 0) + 1
            if counts[s[right]] > counts[maxchar]:
                maxchar = s[right]
            replace = right-left+1-counts[maxchar]  
            while replace > k:
                counts[s[left]] = counts[s[left]] - 1
                for char, c in counts.items():
                    if c > counts[maxchar]:
                        maxchar = char
                left += 1
                replace = right-left+1-counts[maxchar] 
            maxlen = max(maxlen, right-left+1)
            right += 1
        return maxlen
                
                



        


        