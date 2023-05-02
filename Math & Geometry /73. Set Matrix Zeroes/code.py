class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix),len(matrix[0])
        row = [False for i in range(m)]
        column = [False for i in range(n)]
        
        for i in range(m):
           for j in range(n):
               if matrix[i][j] == 0:
                   row[i] = True
                   column[j] = True
        
        for i in range(len(row)):
            if row[i]:
                for j in range(n):
                    matrix[i][j] = 0

        for i in range(len(column)):
            if column[i]:
                for j in range(m):
                    matrix[j][i] = 0