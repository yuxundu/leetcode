class Solution {
    public List<Integer> numIslands2(int m, int n, int[][] positions) {
        // -1 means root does not assigned
        int[] group = new int[m*n];
        Arrays.fill(group,-1);
        List<Integer> ans = new ArrayList<>();
        int count = 0;
        for(int[] p : positions){
            int currIndex = (p[0] * n) + p[1];
            if(group[currIndex] != -1) {
                ans.add(count);
                continue;
            };
            group[currIndex] = currIndex;
            count += 1;
            //up
            int x = p[0] + 1;
            int y = p[1];
  
            if(validateBoundary(m,n,x,y)){
                int destIndex = (x * n) + y;
                if(union(currIndex,destIndex,group)){
                    count -= 1;

                }
            }
            //down
            x = p[0] - 1;
            y = p[1];
            if(validateBoundary(m,n,x,y)){
                int destIndex = (x * n) + y;
                if(union(currIndex,destIndex,group)){
                    count -= 1;

                }
            }
            //right
            x = p[0];
            y = p[1] + 1;     
            if(validateBoundary(m,n,x,y)){
                int destIndex = (x * n) + y;
                if(union(currIndex,destIndex,group)){
                    count -= 1;

                }
            }
            //left
            x = p[0];
            y = p[1] - 1; 
            if(validateBoundary(m,n,x,y)){
                int destIndex = (x * n) + y;
                if(union(currIndex,destIndex,group)){
                    count -= 1;
                }
            }

            ans.add(count);
        } 
        return ans;
    }

    public boolean validateBoundary(int m, int n, int x, int y){
        if(x < 0 || y < 0 || x > m - 1 || y > n - 1){
            return false;
        }
        return true;
    }

    public boolean union(int currIndex,int destIndex,int[] group){
        if(group[destIndex] == -1 ) return false;
        int rootCurrIndex = find(currIndex,group);
        int rootDestIndex = find(destIndex,group);
        if(rootCurrIndex != rootDestIndex){
            group[rootCurrIndex] = rootDestIndex;
            return true;
        }
        return false;
    }

    public int find(int index, int[] group){
        if(group[index] == index) return index;
        return find(group[index],group);

    }
}