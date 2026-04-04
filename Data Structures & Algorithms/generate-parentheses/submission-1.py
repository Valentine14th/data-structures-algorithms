class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def genPar(op, clo):
                if op == clo and op == n:
                    res.append("".join(stack))
                    return
                if op > clo:
                    # can add a clo
                    stack.append(')')
                    genPar(op, clo+1)
                    stack.pop()
                if op < n:
                    # can add op
                    stack.append('(')
                    genPar(op+1, clo)
                    stack.pop()
                return
        genPar(0,0)
        return res
        

                


        