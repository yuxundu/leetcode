class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if(n == 1) return nums[0];
        if(n == 2) return Math.max(nums[0],nums[1]);
        if(n == 3) return Math.max(nums[0],Math.max(nums[1],nums[2]));   
        int[] leftNums = Arrays.copyOfRange(nums, 0, n-1);
        int[] rightNums = Arrays.copyOfRange(nums, 1, n);
        return Math.max(robOne(leftNums),robOne(rightNums));
    }

    public int robOne(int[] nums){
        int n = nums.length;
        int[] dp = new int[n];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0],nums[1]);
        for(int i = 2; i < n; i++){
            dp[i] = Math.max(dp[i-1],nums[i]+dp[i-2]);
        }
        return dp[n-1];
    }
}