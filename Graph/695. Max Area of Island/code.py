class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        visits = set()
        area = 0
        def dfs(r,c):
            if r < 0 or r == rows or c < 0 or c == cols or (r,c) in visits or grid[r][c] == 0:
             return 0
            visits.add((r,c))
            return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c+1) + dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                area = max(area,dfs(r,c))

        return area