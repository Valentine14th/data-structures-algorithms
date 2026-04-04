from functools import reduce
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        for c in t:
            count[c] = count.get(c, 0) - 1
        return reduce(lambda acc, x: acc and x == 0, count.values(), True)
        