class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        out = []

        def recurse(i, current, sum):
            print(current)
            if sum == target:
                if current not in out:
                    out.append(current)
            elif sum > target or i == len(candidates):
                return
            else:
                # use the element
                recurse(i+1, current + [candidates[i]], sum + candidates[i])
                while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                    i += 1
                recurse(i+1, current, sum)

        recurse(0, [], 0)
        return out



        
        