class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        zeros = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.append([i, j])
        
        row = [0]*n
        for i in zeros:
            matrix[i[0]] = row
            for j in range(m):
                matrix[j][i[1]] = 0
        
        