class Solution {
    public int countComponents(int n, int[][] edges) {
        UnionFind unionFind = new UnionFind(n);
        for(int[] edge : edges){
            unionFind.union(edge[0],edge[1]);
        }
        return (int)unionFind.groupCount();
        
    }

    class UnionFind{

        private int[] dp;

        public UnionFind(int n){
            dp = new int[n];
            Arrays.fill(dp,-1);
        }

        public long groupCount(){
            return Arrays.stream(dp).filter( i -> i == -1).count();
        }

        public int findRoot(int x){
            if(dp[x] == -1) return x;

            return findRoot(dp[x]);
        }

        public void union(int x, int y){
            int rootX = findRoot(x);
            int rootY = findRoot(y);
            if(rootX != rootY){
                dp[rootX] = rootY;
            }

        }



    }
}