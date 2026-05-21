class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                ct, ci = stack.pop()
                out[ci] = i-ci
            stack.append((t, i))
        return out





            
        