class UnionFind:
    def __init__(self):
        self.dp = {}
    def findParent(self,x):
        y = self.dp.get(x,x)
        if y != x:
            y = self.dp[x] = self.findParent(y)
        return y
    def union(self,x,y):
        self.dp[self.findParent(x)] = self.findParent(y)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionFind = UnionFind()

        for x,y in edges:
            unionFind.union(x,y)
        
        return len(set(unionFind.findParent(x) for x in range(n)))
