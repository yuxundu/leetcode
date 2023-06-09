class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        columnSet = set()
        positiveDiagonal = set()
        negotiveDiagonal = set()

        board = [["."]*n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in columnSet or (r+c) in positiveDiagonal or (r-c) in negotiveDiagonal:
                    continue
                board[r][c] = "Q"
                columnSet.add(c)
                positiveDiagonal.add(r+c)
                negotiveDiagonal.add(r-c)
                backtrack(r+1)
                board[r][c] = "."
                columnSet.remove(c)
                positiveDiagonal.remove(r+c)
                negotiveDiagonal.remove(r-c)
        
        backtrack(0)


        return res