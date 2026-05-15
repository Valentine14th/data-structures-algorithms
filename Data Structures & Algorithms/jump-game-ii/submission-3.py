class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        nextend = 0
        jump = 0
        if len(nums) <= 1:
            return 0
        for start in range(len(nums)):
            nextend = max(nextend, start+nums[start])
            if nextend >= len(nums)-1:
                return jump+1
            if start == end:
                print("next", end, nextend)
                jump += 1
                end = nextend
        return -1


        