class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights),len(heights[0])
        pSet, aSet = set(), set()

        def dfs(x,y,visited,preHeight):
            if(
                min(x,y) < 0
                or x >= m
                or y >= n
                or (x,y) in visited
                or heights[x][y] < preHeight
            ):
                return
            preHeight = heights[x][y]
            visited.add((x,y))
            dfs(x-1,y,visited,preHeight)
            dfs(x+1,y,visited,preHeight)
            dfs(x,y-1,visited,preHeight)
            dfs(x,y+1,visited,preHeight)
        
        for i in range(m):
            dfs(i,0,pSet,-1)
            dfs(i,n-1,aSet,-1)
        for i in range(n):
            dfs(0,i,pSet,-1)
            dfs(m-1,i,aSet,-1)
        ans = []

        for i in range(m):
            for j in range(n):
                if (i,j) in pSet and (i,j) in aSet:
                    ans.append([i,j])

        return ans


