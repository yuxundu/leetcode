class Solution {
    public int minCost(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        boolean[][] visiting = new boolean[m][n];
        Deque<int[]> deque = new ArrayDeque<>();
        int[][] directions = {{0,0},{0,1},{0,-1},{1,0},{-1,0}};

        deque.add(new int[]{0,0,0});
        //dfs
        while(!deque.isEmpty()){
            int[] item = deque.poll();
            int x = item[0] ,y = item[1], d = item[2];
            if(Math.min(x,y) < 0 || x >= m || y >= n){
                continue;
            }
            if(visiting[x][y]){
                continue;
            }
            if(x == m-1 && y == n-1){
                return d;
            }
            visiting[x][y] = true;
            for(int i = 1; i < 5; i++){
                if(i == grid[x][y]){
                    deque.addFirst(new int[]{x+directions[i][0],y+directions[i][1],d});
                }
                else{
                    deque.add(new int[]{x+directions[i][0],y+directions[i][1],d+1});
                }
            }

        }
        return -1;
    }
}