class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int length = s.length();
        int[] dp = new int[length];
        return subWordBreak(0,s,wordDict,dp);
    }

    public boolean subWordBreak(int index,String s, List<String> wordDict,int[] dp){
        if(dp[index] == -1) return false;
        for(String word : wordDict){
            if(s.startsWith(word)){
                if(s.length() == word.length()) return true;
                if(subWordBreak(index+ word.length(),s.substring(word.length()),wordDict,dp)){
                    return true;
                }
                else{
                    dp[index + word.length()] = -1;
                }
            }
        }
        dp[index] = -1;
        return false;
    }
}