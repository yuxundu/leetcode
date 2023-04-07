class Solution {
    public boolean validTree(int n, int[][] edges) {
        List<List<Integer>> edgeList = new ArrayList<>();
        for(int i = 0; i < n; i++){
            edgeList.add(new ArrayList<Integer>());
        }
        for(int[] edge : edges){
            edgeList.get(edge[0]).add(edge[1]);
            edgeList.get(edge[1]).add(edge[0]);
        }
        Set<Integer> visiting = new HashSet<Integer>();
        if(!dfs(visiting,0,-1,edgeList)){
            return false;
        }

        return visiting.size() == n?true:false;
        
        
    }

    public boolean dfs(Set<Integer> visiting, int index, int pre, List<List<Integer>> edgeList){
        if(visiting.contains(index)) return false;
        visiting.add(index);
        for(Integer edge : edgeList.get(index)){
            if(edge == pre) continue;
            if(!dfs(visiting,edge,index,edgeList)){
                return false;
            }
        }
        return true;
    }
}