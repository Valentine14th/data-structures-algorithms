class Solution:
    def reverseBits(self, n: int) -> int:
        out = ""
        while n > 0:
            bit  = n & 1
            out += str(bit)
            n = n >> 1
        out += "0"*(32-len(out))
        res = 0
        for bit in out:
            res = res * 2 + int(bit)

        print(out)
        return res

        