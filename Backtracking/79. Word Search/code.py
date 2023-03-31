class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        def dfs(x:int,y:int,i:int):
            if i == len(word):
                return True
            if(
                min(x,y) < 0
                or x >= m
                or y >= n
                or word[i] != board[x][y]
                or board[x][y] == '*'
            ):
                return False
            temp = board[x][y]
            board[x][y] = '*'
            if(
                dfs(x-1,y,i+1)
                or dfs(x+1,y,i+1)
                or dfs(x,y-1,i+1)
                or dfs(x,y+1,i+1)

            ):
                return True;
            board[x][y] = temp
            return False
        for i in range(0,m):
            for j in range(0,n):
                if dfs(i,j,0):
                    return True
        return False

            