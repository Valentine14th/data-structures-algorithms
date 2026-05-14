class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        out = []
        out.append([])
        nums.sort()
        def back(i, curr):
            for j in range(i, len(nums)):
                if j > i and nums[j-1] == nums[j]:
                    continue
                curr.append(nums[j])
                out.append(curr.copy())
                back(j+1, curr)
                curr.pop()
        back(0, [])
        return out
        