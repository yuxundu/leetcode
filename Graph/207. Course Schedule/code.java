class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> preList = new ArrayList<>();

        for(int i = 0; i < numCourses; i++){
            preList.add(new ArrayList<Integer>());
        }

        for(int[] prerequisite : prerequisites){
            preList.get(prerequisite[0]).add(prerequisite[1]);
        }
        Set<Integer> path = new HashSet<>();
        for(int i = 0; i < numCourses; i++){
            if(!dfs(path,preList,i)){
                return false;
            }
        }

        return true;
    }

    public boolean dfs(Set<Integer> path,List<List<Integer>> preList, int i){
        if(path.contains(i)) return false;
        if(preList.get(i).size()==0) return true;
        path.add(i);
        for(int pre : preList.get(i)){
            if(!dfs(path,preList,pre)){
                return false;
            }
        }
        path.remove(i);
        preList.set(i,new ArrayList<Integer>());
        return true;

    }


}