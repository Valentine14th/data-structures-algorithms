class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = ""
        end = max(len(word1), len(word2))
        for i in range(end):
            if i < len(word1):
                out += word1[i]
            if i < len(word2):
                out += word2[i]
        return out

        