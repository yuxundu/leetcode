class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(x:int, y:int):
            if(
                min(x,y) < 0 
                or x >= m 
                or y >= n 
                or grid[x][y] == '2' 
                or grid[x][y] == '0'
            ):
                return
            grid[x][y] = '2'
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)

        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i,j)
        return ans
        