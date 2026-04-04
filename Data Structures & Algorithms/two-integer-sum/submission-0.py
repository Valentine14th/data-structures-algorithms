class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = {}
        for i, n in enumerate(nums):
            if (target - n) in first:
                return [first[target-n], i]
            else:
                first[n] = i
        