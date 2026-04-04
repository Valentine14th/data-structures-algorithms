class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        # we want nums[i] + nums[j] == -nums[k]
        out = []
        for k in range(len(nums)):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k-1]:
                continue
            target = -nums[k]
            left = k+1
            right = len(nums) - 1
            print(target)
            while left < right:
                s = nums[left] + nums[right]
                print(nums[left], nums[right])
                if s > target:
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    print("hey", s)
                    out.append([nums[k], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < len(nums) and nums[left] == nums[left-1]:
                        left += 1
        return out
                



        