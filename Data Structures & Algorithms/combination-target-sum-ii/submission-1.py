class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        out = []
        def recurse(i, current, sum):
            print(current)
            if sum == target:
                if current not in out:
                    out.append(current)
            elif sum > target or i == len(candidates):
                return
            else:
                recurse(i+1, sorted(current + [candidates[i]]), sum + candidates[i])
                recurse(i+1, current, sum)

        recurse(0, [], 0)
        return out



        
        