class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        time, fresh = 0,0
        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        dictions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c  = q.popleft()
                for dr,dc in dictions:
                    dr,dc = r+dr,c+dc
                    if dr < 0 or dr == rows or dc < 0 or dc == cols or grid[dr][dc] != 1:
                        continue
                    grid[dr][dc] = 2
                    q.append((dr,dc))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1
        
        
