class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacent = { i :[] for i in range(n)}
        for edge in edges:
            adjacent[edge[0]].append(edge[1])
            adjacent[edge[1]].append(edge[0])
        
        visiting = set()

        def dfs(i:int, pre:int):
            if i in visiting:
                return False
            visiting.add(i)

            for value in adjacent[i]:
                if value == pre:
                    continue
                if not dfs(value,i):
                    return False
            
            return True
        
        if not dfs(0,-1):
            return False;

        return True if len(visiting) == n else False