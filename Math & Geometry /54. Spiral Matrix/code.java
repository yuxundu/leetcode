class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int l = 0, r = n, t = 0, b = m;
        List<Integer> ans = new ArrayList<>(); 
        while (l < r && t < b){
            for(int i = l; i < r; i++){
                ans.add(matrix[t][i]);
            }
            t++;
            for(int i = t ; i < b; i++){
                ans.add(matrix[i][r-1]);
            }
            r--;
            if(l >= r || t >= b){
                break;
            }
            for(int i = r-1 ; i >= l; i--){
                ans.add(matrix[b-1][i]);
            }
            b--;
            for(int i = b-1 ; i >= t; i--){
                ans.add(matrix[i][l]);
            }
            l++;


        }
        return ans;
        
    }
}