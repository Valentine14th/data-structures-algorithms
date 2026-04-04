class Solution:
    def longestPalindrome(self, s: str) -> str:
        lr = -1
        ll = -1
        maxi = -1
        def recurse(start, end):
            if start < 0 or end > len(s) - 1 or s[start] != s[end]:
                (outl, outr) = (start+1, end-1) if start+1 <= end-1 else (start, end)
                print("base case", outl, outr)
                return (outl, outr)
            else: # s[start] == s[end]:
                return recurse(start-1, end + 1)
        i = 0
        while i < len(s):
            print("recruse", i)
            (l, r) = recurse(i, i)
            if r-l+1 > maxi:
                maxi = r-l+1
                lr = r
                ll = l
            if i+1 < len(s) and s[i] == s[i+1]:
                (le, re) = recurse(i, i+1)
                if re-le+1 > maxi:
                    maxi = re-le+1
                    lr = re
                    ll = le
            i += 1
        return s[ll:lr+1]
        
        

        