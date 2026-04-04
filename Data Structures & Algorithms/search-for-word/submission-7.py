class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        out = False
        width = len(board[0])
        height = len(board)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(char_i: int, ci: int, cj: int, seen: List[List[int]]):
            nonlocal out
            if char_i > len(word) - 1:
                out = True
                #print("word")
                return
            for v, h in directions:
                iv = ci + v
                jh = cj + h
                #print("check", iv, jh)
                #print("test", char_i, word[char_i], iv, jh)
                if iv >= 0 and iv < height and jh >= 0 and jh < width and [iv, jh] not in seen and board[iv][jh] == word[char_i]:
                        #visited[iv][jh] = True
                        print("found", word[char_i], iv, jh, seen)
                        dfs(char_i+1, iv, jh, seen + [[iv, jh]])
        
            return
        
        for i in range(height):
            for j in range(width):
                if out:
                    return out
                if board[i][j] == word[0]:
                    print("found first letter", i, j)
                    #visited = [[False for a in range(width)] for b in range(height)]
                    #visited[i][j] = True
                    dfs(1, i, j, [[i, j]])
        return out
        




            