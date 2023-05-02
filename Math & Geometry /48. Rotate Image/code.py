class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        left,right= 0, n-1
        while left < right:
            for i in range(right-left):
                top,bottom = left,right
                temp = matrix[top+i][left]
                matrix[top+i][left] = matrix[bottom][left+i]
                matrix[bottom][left+i] = matrix[bottom-i][right]
                matrix[bottom-i][right] = matrix[top][right-i]
                matrix[top][right-i]=temp

            left += 1
            right -= 1

        return matrix


        