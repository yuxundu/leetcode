class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>>ans = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        dfs(candidates,target,ans,0,path,0);
        return ans;
    }

    public void dfs(int[] candidates, int target,
     List<List<Integer>>ans, int i, List<Integer> path, int total){
         if(total == target){
             ans.add(new ArrayList<>(path));
             return;
         }
         if(i >= candidates.length || total > target) return;

         path.add(candidates[i]);
         dfs(candidates,target,ans,i,path,total+candidates[i]);
         path.remove(path.size()-1);
         dfs(candidates,target,ans,i+1,path,total);
    }
}