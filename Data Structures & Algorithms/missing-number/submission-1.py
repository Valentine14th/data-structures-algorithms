class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tot = sum(nums)
        should = sum(range(len(nums)+1))
        return should - tot

        