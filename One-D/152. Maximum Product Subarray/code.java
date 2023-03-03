class Solution {
    public int maxProduct(int[] nums) {
       
        int max = nums[0], min = nums[0];
        int ans = nums[0];
        for(int i = 1; i < nums.length; i++){
            int tempmax = Math.max(nums[i],Math.max(nums[i]*max,nums[i]*min));
            int tempmin = Math.min(nums[i],Math.min(nums[i]*max,nums[i]*min));
            
            max = tempmax;
            min = tempmin;

            ans = Math.max(max,ans);
        }
        return ans;
        
    }
}