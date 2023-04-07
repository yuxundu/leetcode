class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int m = heights.length, n = heights[0].length;
        Set<String> pacificSet = new HashSet<>(), atlanticSet = new HashSet<>();
        for(int i = 0; i < m; i++){
            dfs(m,n,i,0,pacificSet,-1,heights);
            dfs(m,n,i,n-1,atlanticSet,-1,heights);
        }

        for(int i = 0; i < n; i++){
            dfs(m,n,0,i,pacificSet,-1,heights);
            dfs(m,n,m-1,i,atlanticSet,-1,heights);
        }
        List<List<Integer>> ans = new ArrayList<>();
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(pacificSet.contains(i+":"+j) && atlanticSet.contains(i+":"+j)){
                    List<Integer> cell = new ArrayList<>();
                    cell.add(i);
                    cell.add(j);
                    ans.add(cell);
                }
            }
        }
        return ans;
        
    }

    public void dfs(int m, int n, int x, int y, Set<String> visitedSet,int preHeight,int[][] heights){
        if(x < 0 || y < 0 || x >= m || y >= n || visitedSet.contains(x+":"+y) || heights[x][y] < preHeight){
            return;
        }
        visitedSet.add(x+":"+y);
        preHeight = heights[x][y];
        dfs(m,n,x-1,y,visitedSet,preHeight,heights);
        dfs(m,n,x+1,y,visitedSet,preHeight,heights);
        dfs(m,n,x,y-1,visitedSet,preHeight,heights);
        dfs(m,n,x,y+1,visitedSet,preHeight,heights);
    }
}