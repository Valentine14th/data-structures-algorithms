class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def recurse(currm, currn):
            if currm == 0 and currn == 0:
                return 1
            if currm < 0 or currn < 0:
                return 0
            else:
                return recurse(currm-1, currn) + recurse(currm, currn-1)
        return recurse(m-1, n-1)
            
        