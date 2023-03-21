class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];
        int prefix = 1;
        for(int i = 0; i < nums.length; i++){
            prefix = prefix * ( i > 0? nums[i-1]:1);
            ans[i] = prefix;
        }
        int postfix = 1;
        for(int i = nums.length - 1; i >= 0; i--){
             postfix = postfix * ( i ==  nums.length - 1? 1 : nums[i +1]);
             ans[i] = ans[i] * postfix;
         }
         return ans;
    }
}