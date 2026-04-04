class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [[-1] * 2 for i in range(len(nums))]

        def recurse(current: int, first: int):
            if current >= len(nums):
                return 0
            else:
                if memo[current][first] != -1:
                    return memo[current][first]
                if current == 0:
                    memo[current][first] = max(nums[current]+recurse(current+2, 0), recurse(current+1, 1))
                elif current == len(nums) - 1:
                    memo[current][first] = max(recurse(current+1, first), nums[current]+recurse(current+2, first)) if first == 1 else recurse(current+1, first)
                else:
                    memo[current][first] = max(recurse(current+1, first), nums[current]+recurse(current+2, first))
                return memo[current][first]
        
        return recurse(0, 0)
                

        