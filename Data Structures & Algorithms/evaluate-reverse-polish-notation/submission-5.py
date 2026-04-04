class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return self.getNumber(tokens[0])
        stack = []
        i = 0
        while i < len(tokens):
            char = tokens[i]
            if char not in ['+', '-', '*', '/']:
                stack.append(self.getNumber(tokens[i]))
            else: 
                right = stack.pop()
                left = stack.pop()
                print(left, char, right)
                match char:
                    case '+':
                        left = left + right
                    case '-':
                        left = left - right
                    case '*':
                        left = left * right
                    case '/':
                        left = int(left / right)
                print(left)
                stack.append(left)
            i += 1
        return stack.pop()

    def getNumber(self, s : str) -> int:
        i = 0
        out = 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        while i < len(s):
            num = ord(s[i]) - ord('0')
            out += num * 10 ** (len(s) - i - 1)
            i += 1
        return sign * out



        

        