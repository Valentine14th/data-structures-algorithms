class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {'(': ')', '{':'}', '[':']'}
        for l in s:
            if l == '(' or l == '{' or l == '[':
                stack.append(l)
            if l == ')' or l == '}' or l == ']':
                if not stack:
                    return False
                if parenthesis[stack[-1]] != l:
                    return False
                else:
                    stack.pop()
        return not stack


        