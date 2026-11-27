class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        zeros = []
        row = [0]*n
        for i in range(m):
            zeroed = False
            for j in range(n):
                if matrix[i][j] == 0:
                    if j not in zeros:
                        zeros.append(j)
                    zeroed = True
            if zeroed:
                matrix[i] = row

        
        for i in zeros:
            for j in range(m):
                matrix[j][i] = 0
        
        