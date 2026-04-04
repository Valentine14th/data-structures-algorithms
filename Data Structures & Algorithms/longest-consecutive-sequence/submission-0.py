class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        current_max = 0
        for i in nums:
            if i-1 not in numset:
                length = 1
                while i + length in numset:
                    length += 1
                current_max = length if length > current_max else current_max
        return current_max




        