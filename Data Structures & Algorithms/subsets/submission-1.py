class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        def dfs(subset, i):
            if i >= len(nums):
                out.append(subset)
                return
            dfs(subset + [nums[i]], i+1)
            dfs(subset, i+1)
        dfs([], 0)
        return out




        
        
        