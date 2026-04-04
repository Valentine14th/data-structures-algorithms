class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def rec(curr: List[int], nums: List[int]):
            if len(nums) == 0:
                print(curr)
                return [curr]
            return rec(curr+[nums[0]], nums[1:]) + rec(curr, nums[1:])
        return rec([], nums)


        
        
        