class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        used = [False]*len(nums)
        maxl = len(nums)
        def back(curr):
            if len(curr) == maxl:
                #print(curr)
                out.append(curr.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    curr.append(nums[i])
                    used[i] = True
                    back(curr)
                    used[i] = False
                    curr.pop()
        back([])
        return out
                

        