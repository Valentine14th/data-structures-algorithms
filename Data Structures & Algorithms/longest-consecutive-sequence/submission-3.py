class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for n in numset:
            if n-1 not in numset:
                i = n+1
                currl = 1
                while i in numset:
                    currl += 1
                    i += 1
                longest = max(longest, currl)
        return longest

        



        