class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { i:[] for i in range(numCourses)}
        for c,p in prerequisites:
            preMap[c].append(p)
        visit,cycle = set(),set()
        res = []
        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            cycle.add(c)
            for pre in preMap[c]:
                if not dfs(pre):
                    return False
            cycle.remove(c)
            visit.add(c)
            res.append(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []



        return res