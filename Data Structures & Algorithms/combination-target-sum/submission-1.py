class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        out = []
        def recurse(i, comb, add):
            if add == target:
                out.append(comb.copy())
                return
            if i >= len(nums) or add > target:
                return
            recurse(i+1, comb.copy(), add)
            recurse(i, comb + [nums[i]], add + nums[i])
    
        recurse(0, [], 0)
        return out



            
        



        