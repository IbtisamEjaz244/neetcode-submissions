class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            row = []
            for j in i:
                if j != ".":
                    if j in row:
                        return False
                    else:
                        row.append(j)
        
        for i in range(9):
            col = []
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in col:
                        return False
                    else:
                        col.append(board[j][i])
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub = []
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] != ".":
                            if board[i+k][j+l] in sub:
                                return False
                            else:
                                sub.append(board[i+k][j+l])
        
        return True
