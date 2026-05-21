class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        candidates.sort()
        def back(i, curr, currsum):
            if currsum == target:
                out.append(curr.copy())
                return
            if currsum > target:
                return
            for c in range(i, len(candidates)):
                if c > i and candidates[c-1] == candidates[c]:
                    continue
                curr.append(candidates[c])
                currsum += candidates[c]
                back(c+1, curr, currsum)
                curr.pop()
                currsum -= candidates[c]
        back(0, [], 0)
        return out
            
        