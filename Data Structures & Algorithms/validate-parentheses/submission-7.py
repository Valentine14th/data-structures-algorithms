class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(': ')', '{':'}', '[':']'}
        for c in s:
            if c in brackets.keys():
                stack.append(c)
            elif c in brackets.values():
                if len(stack) <= 0:
                    return False
                last = stack.pop() 
                if brackets[last] != c:
                    return False
        return len(stack) == 0
        