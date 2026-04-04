class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        should = 0
        tot = 0
        for i in range(len(nums)+1):
            if i != len(nums):
                tot += nums[i]
            should += i
        print(should)
        return should - tot

        