class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out = out + str(len(s)) + "#" + s
        return out

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        out = []
        i = 0
        strlen = ""
        while i < len(s):
            while s[i] != '#':
                strlen += s[i]
                i += 1
            i += 1
            le : int = int(strlen)
            if le == 0:
                out.append("")
            else:
                out.append(s[i:i+le])
                i += le
            strlen = ""
        return out




