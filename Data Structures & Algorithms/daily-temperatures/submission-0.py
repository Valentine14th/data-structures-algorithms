class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(0, temperatures[0])]
        out = [0 for i in range(len(temperatures))]
        for i in range(1, len(temperatures)):
            if temperatures[i] <= stack[-1][1]:
                stack.append((i, temperatures[i]))
                print("add", stack)
            else:
                while len(stack) > 0 and stack[-1][1] < temperatures[i]:
                    ind, val = stack.pop()
                    out[ind] = i-ind
                stack.append((i, temperatures[i]))
                print("remove", stack, out)
        return out







        