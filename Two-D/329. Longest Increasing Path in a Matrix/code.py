class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows,cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r,c,preValue):
            if (r  <0 or r > rows-1 or c < 0 or c > cols-1 or matrix[r][c] <= preValue):
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            res = 1
            res = max(res,1+dfs(r+1,c,matrix[r][c]))
            res = max(res,1+dfs(r-1,c,matrix[r][c]))
            res = max(res,1+dfs(r,c+1,matrix[r][c]))
            res = max(res,1+dfs(r,c-1,matrix[r][c]))
            dp[(r,c)] = res
            return dp[(r,c)]

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,-1)
        
        return max(dp.values())



