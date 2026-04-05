class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j] == 0):
                    for k in range(len(matrix)):
                        matrix[k][j] = 'D' if matrix[k][j] != 0 else matrix[k][j]
                    for k in range(len(matrix[0])):
                        matrix[i][k] = 'D' if matrix[i][k] != 0 else matrix[i][k]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j] == 'D'):
                    matrix[i][j] = 0
        