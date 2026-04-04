class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[-1]*n for i in range(m)]
        paths[0][0] = 1

        def recurse(currm, currn):
            if currm == 0 and currn == 0:
                return paths[0][0]
            if currm < 0 or currn < 0:
                return 0
            else:
                if paths[currm][currn] != -1:
                    return paths[currm][currn]

                paths[currm][currn] = recurse(currm-1, currn) + recurse(currm, currn-1)
                return paths[currm][currn]
        return recurse(m-1, n-1)
            
        