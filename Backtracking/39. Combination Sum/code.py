class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(i:int, path: List[int], total:int):
            if total == target:
                ans.append(path.copy()) 
                return
            if i >= len(candidates) or total > target:
                return
            path.append(candidates[i])
            dfs(i,path,total+candidates[i]);
            path.pop()
            dfs(i+1,path,total)

        dfs(0,[],0)
        return ans