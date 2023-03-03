class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        int[] dp = new int[n+1];
        dp[0] = 1;
        if(s.charAt(0) == '0'){
            return 0;
        }
        dp[1] = 1;
        for(int i = 2; i <= n; i++){
            char firstCh = s.charAt(i-1);
            char secondCh = s.charAt(i-2);
            if(firstCh == '0'){
                if(secondCh == '1' || secondCh == '2'){
                    dp[i] = dp[i-2];
                }
                else{
                    return 0;
                }
            }
            else{
                if((secondCh == '1' || (secondCh == '2' && Character.getNumericValue(firstCh) < 7))){
                    dp[i] = dp[i-1] + dp[i-2];
                }
                else{
                    dp[i] = dp[i-1];
                }
            }
        }
        return dp[n];
    }
}