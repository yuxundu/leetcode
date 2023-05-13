class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, column = len(matrix), len(matrix[0])
        top,bottom = 0, row-1
        while top <= bottom:
            mid = top + (bottom - top)//2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][column-1]:
                top = mid + 1
            else:
                break
        if top > bottom:
            return False
        row = top + (bottom-top)//2
        l, r = 0, column-1
        while l <= r:
            mid = l + (r - l)//2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True

        return False


