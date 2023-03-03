class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount+1];
        Arrays.fill(dp,-1);
        dp[0] = 0;
        for(int i = 1; i <= amount; i++){
            subCoinChange(i,coins,dp);
        }

        return dp[amount];
    }

    public void subCoinChange(int target,int[] coins,int[] dp){

        for(int i = 0; i < coins.length; i++){
            int coinValue = coins[i];
            int remain = target - coinValue;
            if(remain < 0 || dp[remain] == -1) continue;
            int path = dp[remain] + 1;

            dp[target] = dp[target] == -1? path : Math.min(path,dp[target]);
        }
        

    }
}