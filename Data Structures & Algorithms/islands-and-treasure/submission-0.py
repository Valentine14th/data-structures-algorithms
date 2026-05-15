class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        h = len(grid)
        w = len(grid[0])
        
        def dfs(start):
            visited = set()
            q = deque()
            q.append(start)
            dist = 0
            while q:
                l = len(q)
                dist += 1
                for _ in range(l):
                    y, x = q.popleft()
                    for dy, dx in directions:
                        ny, nx = dy+y, dx+x
                        if 0 <= ny < h and 0 <= nx < w and (ny,nx) not in visited and grid[ny][nx] != -1:
                            visited.add((ny, nx))
                            grid[ny][nx] = min(grid[ny][nx], dist)
                            q.append((ny, nx))
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0:
                    dfs((i,j))                            

        