class Solution:
    # binary search looking for first number bigger or equal to target
    def findMin(self, nums: List[int]) -> int:
        # looking for value where left neighbor is bigger
        # ie looking for value where right neighbor is smaller
        left = 0
        right = len(nums) - 1
        while left < right:
            print(left, right)
            mid = (right+left) // 2
            curr = nums[mid]
            nextt = nums[(mid+1)%len(nums)]
            #if nextt < curr:
            #    return nextt
            # ordered on the right, only increasing, we don't care
            if curr < nums[right]:
                right = mid
            # not ordered on the right, then definitely there
            else:
                left = mid+1
        return nums[left]
            
            
        