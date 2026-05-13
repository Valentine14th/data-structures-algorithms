class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0]*len(board)
        cols = [0]*len(board)
        square = [0]*(len(board)**2)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                bit = 1 << int(board[i][j])
                if rows[j] & bit > 0:
                    return False
                rows[j] = rows[j] | bit
                if cols[i] & bit > 0:
                    return False
                cols[i] = cols[i] | bit
                if square[(i//3)*len(board)+(j//3)] & bit > 0:
                    return False
                square[(i//3)*len(board)+(j//3)] = square[(i//3)*len(board)+(j//3)] | bit
        return True
        