class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += str(len(s)) + ":" + s
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        while len(s) > 0:
            l, rest = s.split(':', 1)
            out.append(rest[:int(l)])
            s = rest[int(l):]
        return out


