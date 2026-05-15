class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        w = len(grid[0])
        h = len(grid)

        def bfs(start):
            q = deque()
            q.append(start)
            grid[start[0]][start[1]] = 0
            size = 0
            while q:
                y, x = q.popleft()
                size += 1
                for dy, dx in directions:
                    ny, nx = dy+y, dx+x
                    if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == 1:
                        grid[ny][nx] = 0
                        q.append((ny, nx))
            return size
        maxi = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    s = bfs((i, j))
                    print((i,j), s)
                    maxi = max(maxi, s)
        return maxi


        