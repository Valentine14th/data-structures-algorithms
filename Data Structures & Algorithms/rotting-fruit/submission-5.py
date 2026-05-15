class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # start from all rotten fruits, 
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        h = len(grid)
        w = len(grid[0])
        def bfs(starts):
            #visited = set()
            q = deque()
            for s in starts:
                q.append(s)
                grid[s[0]][s[1]] = 2
                #visited.add(s)
            dist = -1
            while q:
                l = len(q)
                dist += 1
                for _ in range(l):
                    y, x = q.popleft()
                    for dy, dx in directions:
                        ny, nx = dy+y, dx+x
                        if 0 <= ny < h and 0<=nx<w and grid[ny][nx] == 1:
                            print(i,j, "rotten", dist)
                            grid[ny][nx] = 2
                            #visited.add((ny, nx))
                            q.append((ny,nx))
            return dist
        rots = []
        fresh = False
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 2:
                    rots.append((i,j))
                elif grid[i][j] == 1:
                    fresh = True
        if len(rots) == 0 and not fresh:
            return 0
        time = bfs(rots)
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    return -1
        return time




        