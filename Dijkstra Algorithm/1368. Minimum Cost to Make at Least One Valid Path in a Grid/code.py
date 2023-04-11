from collections import deque

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dirs = [[0,0], [0,1], [0,-1], [1,0], [-1,0]]
        visted = [ [False for x in range(n)] for y in range(m)]
        print(visted)
        queue = deque()
        queue.append([0,0,0])
        while len(queue) > 0:
            item = queue.popleft()
            if min(item[0],item[1]) < 0 or item[0] >=m or item[1] >= n:
                continue
            if visted[item[0]][item[1]]:
                continue
            if item[0] == m-1 and item[1] == n-1:
                return item[2]
            visted[item[0]][item[1]] = True
            for i in range(1,5):
                nextX, nextY = item[0] + dirs[i][0], item[1] + dirs[i][1]
                if i == grid[item[0]][item[1]]:
                 queue.appendleft([nextX, nextY, item[2]])
                else:
                 queue.append([nextX, nextY, item[2]+1])   

        return -1

