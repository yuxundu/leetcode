class Solution {
    public int findMin(int[] nums) {
        int length = nums.length;
        if(length == 1){
            return nums[0];
        }
        int left = 0;
        int right = length - 1;
        
        while(left < right){
            if(right - left == 1){
                return Math.min(nums[left],nums[right]);
            }
            int mid = (left+right) / 2;

            if(nums[left] < nums[mid] && nums[mid] < nums[right]){
                return nums[left];
            }
            else if(nums[left] > nums[mid]){
                right = mid;
            }
            else{
                left = mid;
            }
             
        }

        return 0;
    }
}