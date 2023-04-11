class Solution {
    public int swimInWater(int[][] grid) {
        int n = grid.length;
        PriorityQueue<int[]> min_heap = new PriorityQueue<>((x,y) -> {
            return Integer.compare(x[0],y[0]);
        });
        min_heap.add(new int[]{grid[0][0],0,0});
        Set<String> visited = new HashSet<>();
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}}; 
        

        while(!min_heap.isEmpty()){
            int[] data = min_heap.poll();
            if(visited.contains(data[1]+":"+data[2])){
                continue;
            }
            if(data[1] == data[2] && data[1]  == n-1){
                return data[0];
            }
            visited.add(data[1]+":"+data[2]);

            for(int i = 0; i < 4; i++){
                int x = data[1]+dirs[i][0], y = data[2]+dirs[i][1];
                if(Math.min(x,y) <0 || x >= n || y >=n){
                    continue;
                }

                min_heap.add(new int[]{Math.max(data[0],grid[x][y]),x,y});

            }

        }
        return -1;

        
    }
}