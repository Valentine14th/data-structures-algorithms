class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        width = len(heights[0])
        height = len(heights)
        # init two solutions
        pacific = set()
        atlantic = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        def dfs(curri, currj, ocean):
            if (curri, currj) in ocean:
                return
            else:
                ocean.add((curri, currj))
                for dv, dh in directions:
                    idv = curri + dv
                    jdh = currj + dh
                    if idv >= 0 and jdh >= 0 and idv < height and jdh < width and heights[idv][jdh] >= heights[curri][currj]:
                        dfs(idv, jdh, ocean)
                        print("reach", idv, jdh)
                return
        for i in range(height):
            for j in range(width):
                if i == 0 or j == 0:
                    print("start pacific", i, j)
                    dfs(i, j, pacific)
                if i == height - 1 or j == width - 1:
                    print("start atlantic", i, j)
                    dfs(i, j, atlantic)
        print(pacific)
        print(atlantic)
        return list(pacific.intersection(atlantic))


            
        
        