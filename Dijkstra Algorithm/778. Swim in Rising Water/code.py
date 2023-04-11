import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        queue = []
        heapq.heappush(queue,(grid[0][0],0,0))
        visited = set()
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        while len(queue) > 0:
            data = heapq.heappop(queue)
            if (data[1],data[2]) in visited:
                continue
            if data[1] == data[2] and data[1] == len(grid) -1:
                return data[0]
            visited.add((data[1],data[2]))
            for a,b in dirs:
                x,y = data[1]+a,data[2]+b
                if min(x,y) < 0 or x >= len(grid) or y >= len(grid):
                    continue
                heapq.heappush(queue,(max(data[0],grid[x][y]),x,y))
            

        return -1
