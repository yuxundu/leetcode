class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [ i for i in range(len(edges)+1)]
        rank = [ 1 for i in range(len(edges)+1)]
        def find(p):
            if p == par[p]:
                return p
            return find(par[p])
        def union(p1,p2):
            root1,root2 = find(p1),find(p2)
            if root1 == root2:
                return False
            if rank[root1] > rank[root2]:
                par[root2] = root1
                rank[root1] += 1
            else:
                par[root1] = root2
                rank[root2] += 1
            return True
        for p1,p2 in edges:
            if not union(p1,p2):
                return [p1,p2]
        return []



        print(par)
        print(rank)
        return []
