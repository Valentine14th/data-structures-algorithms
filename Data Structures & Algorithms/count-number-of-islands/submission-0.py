class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        height = len(grid)
        width = len(grid[0])
        seen = [([0] * width)for i in range(height)]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0
        for i in range(height):
            for j in range(width):
                # if not seen and an island
                if not seen[i][j]:
                    seen[i][j] = 1
                    # start bfs
                    if grid[i][j] == "1":
                        islands += 1
                        print("new island", i, j)
                        queue = deque()
                        queue.append((i,j))
                        while len(queue) > 0:
                            r, c = queue.popleft()
                            seen[r][c] = 1
                            for d in directions:
                                nr = r + d[0]
                                nc = c + d[1]
                                if 0 <= nr < height and 0 <= nc < width and seen[nr][nc] != 1 and grid[nr][nc] == '1':
                                    queue.append((nr, nc))
        return islands




        