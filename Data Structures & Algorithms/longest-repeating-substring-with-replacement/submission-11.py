class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counts = {'A': 0}
        l = 0
        r = 0
        currentmax = 0
        longest = 0
        while l <= r and r < len(s) and l < len(s):
            # add the counts of what is at r
            counts[s[r]] = 1 + counts.get(s[r], 0)
            # update the maximum count element
            if currentmax < counts[s[r]]:
                print("current max", s[r], counts[s[r]])
                currentmax = counts[s[r]]
            # if need to replace too many, move l and count
            while r - l + 1 - currentmax > k:
                counts[s[l]] -= 1
                l += 1
            # update longest because now valid
            longest = max(longest, r-l+1)
            # update r
            r += 1

        return longest
                    









        