class Solution {
    public int maxSubArray(int[] nums) {
        int ans = nums[0];
        int total = 0;
         for(int n : nums){
             total = total + n;
             ans = Math.max(ans,total);
             if(total < 0){
                 total = 0;
             }
         }
         return ans;
    }
}