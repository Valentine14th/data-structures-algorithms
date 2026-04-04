class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = nums[0]
        right_pointer = len(nums) - 2
        end = len(nums)-1

        while end > 0 and right_pointer >= 0:
            while nums[right_pointer] < end - right_pointer and right_pointer >= 0:
                right_pointer -= 1
            end = right_pointer
            right_pointer -= 1

        return end == 0
        





                


            

[1,3,3,0,2,1]

        
        
        