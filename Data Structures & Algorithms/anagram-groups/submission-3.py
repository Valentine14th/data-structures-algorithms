class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        for s in strs:
            alpha = [0] * 26
            for c in s:
                alpha[ord(c)-ord('a')] += 1
            tu = tuple(alpha)
            ana[tu] = ana.get(tu, []) + [s]
        print(len(ana))
        return [l for l in ana.values()]
        