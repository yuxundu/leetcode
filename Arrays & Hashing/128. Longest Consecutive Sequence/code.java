class Solution {
    public int longestConsecutive(int[] nums) {
        int ans = 0;
        Set<Integer> numsSet = new HashSet<>();

        for(int num : nums){
            numsSet.add(num);
        }

        for(int i = 0; i < nums.length; i++){
            if(!numsSet.contains(nums[i]-1)){
                int num = nums[i]+1;
                int length = 1;
                while(numsSet.contains(num)){
                    num++;
                    length++;
                }
                ans = Math.max(length,ans);
            }
        }


        return ans;
    }
}