class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8":"tuv",
            "9": "wxyz"
        }
        out = []
        def back(i, curr):
            if i >= len(digits):
                out.append("".join(curr))
                return 
            for d in letters[digits[i]]:
                curr.append(d)
                back(i+1, curr)
                curr.pop()
        if len(digits) == 0:
            return []
        back(0, [])
        return out
        

        