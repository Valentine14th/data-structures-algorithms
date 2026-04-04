class Solution:
    def rob(self, nums: List[int]) -> int:
        memorization = [-1 for i in range(len(nums))]
        def recurse(start: int) -> int:
            if start >= len(nums):
                return 0
            else:
                if memorization[start] != -1:
                    return memorization[start]
                memorization[start] = max(recurse(start+1), nums[start] + recurse(start+2))
                return memorization[start]

        return recurse(0)


        