class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}
        for i, n in enumerate(nums):
            if n in need:
                return [need[n], i]
            need[target-n] = i
        