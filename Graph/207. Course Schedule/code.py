class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        
        for i,j in prerequisites:
            preMap[i].append(j)
        
        visiting = set()

        def dfs(i:int) -> bool:
            if i in visiting:
                return False
            if len(preMap[i]) == 0:
                return True
            
            visiting.add(i)

            for  pre in preMap[i]:
                if not dfs(pre):
                    return False
            
            visiting.remove(i)
            preMap[i] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


        