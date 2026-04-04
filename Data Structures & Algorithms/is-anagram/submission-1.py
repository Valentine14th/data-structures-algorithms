class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        let = {}
        if len(s) != len(t):
            return False
        for c in s:
            if let.get(c):
                let[c] = let[c] + 1
            else:
                let[c] = 1
        for c in t:
            if let.get(c) and let[c] > 0:
                let[c] = let[c] - 1
        for out in let.values():
            if out != 0:
                return False
        return True

        

        