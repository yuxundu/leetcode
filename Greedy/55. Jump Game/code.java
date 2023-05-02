class Solution {
    public boolean canJump(int[] nums) {
        int goalP = nums.length - 1;

        for( int i =  nums.length - 2; i >= 0; i--){
            if(nums[i] >= goalP-i){
                goalP = i;
            }
        }
        return goalP == 0?true:false;
        
    }
}