class Solution {
    public int[] countBits(int n) {
        int[] res = new int[n+1];
        for(int i = 0; i <= n; i++){
            int count = 0;
            int j = i;
            while(j!= 0){
                j &= j-1;
                count++;
            }
            res[i]=count;
        }
        return res;
    }
}