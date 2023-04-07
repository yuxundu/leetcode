class Solution {
    public int numIslands(char[][] grid) {
        int ans = 0;
        for(int x = 0; x < grid.length; x++){
            for(int y = 0; y < grid[0].length; y++){
                if(grid[x][y] == '1'){
                    ans++;
                    dfs(grid,x,y);
                }
            }
        }
        return ans; 
    }

    public void dfs(char[][] grid, int x, int y){
        if(x < 0 || y < 0 || x >= grid.length || y >= grid[0].length 
        || grid[x][y] == '2' || grid[x][y] == '0'){
            return;
        }
        grid[x][y] = '2';
        dfs(grid,x-1,y);
        dfs(grid,x+1,y);
        dfs(grid,x,y-1);
        dfs(grid,x,y+1);
    }
}