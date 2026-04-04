class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        while left < right:
            print(left, right)
            mid = (right+left) // 2
            print(mid)
            if target == nums[mid]:
                return mid
            # right part sorted
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    print("correct?")
                    left = mid+1
                else:
                    right = mid
            # left sorted
            else:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    print("yes?")
                    left = mid+1
        print("final", left, right)
        return right if nums[right] == target else -1


        