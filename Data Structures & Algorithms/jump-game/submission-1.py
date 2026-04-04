class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            print(i)
            if i + nums[i] >= curr:
                print("new", i)
                curr = i
        return curr == 0

        