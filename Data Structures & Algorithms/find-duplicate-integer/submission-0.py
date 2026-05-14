class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = 0
        for n in nums:
            bit = 1 << n
            if seen & bit > 0:
                return n
            seen = seen | bit
        return -1

        