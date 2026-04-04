class Solution:
    def countBits(self, n: int) -> List[int]:
        def to_bits(n):
            if n == 0:
                return "0"
            res = ""
            while n > 0:
                bit = n & 1
                res = ('1' if bit else '0') + res
                n = n >> 1
            print(res)
            return res
        out = []
        for i in range(n+1):
            out.append(to_bits(i).count('1'))
        return out



        