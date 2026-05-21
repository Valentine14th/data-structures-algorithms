class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # 3sum => a + b + c = 0 <=> a + b = -c
        out = []
        i = 0
        while i < len(nums):
            while i > 0 and i < len(nums)-1 and nums[i] == nums[i-1]:
                i += 1
            c = nums[i]
            left = i+1
            right = len(nums)-1

            while left < right:
                curr = nums[left] + nums[right]
                if curr == -c:
                    out.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1 
                elif curr < -c:
                    left += 1
                else:
                    right -= 1
            i += 1
        return out
        