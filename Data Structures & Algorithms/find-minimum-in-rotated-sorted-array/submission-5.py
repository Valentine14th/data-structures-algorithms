class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        mid = len(nums) // 2
        # while not found cut (check edge)
        while left < right:
            mid = left + (right - left) // 2
            if nums[right] < nums[mid]:
                #search right
                left = mid + 1
            else:
                # search left
                right = mid
        return nums[left]
        