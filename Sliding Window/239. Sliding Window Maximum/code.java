class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        List<Integer> output = new ArrayList<>();
        Deque<Integer> q = new ArrayDeque<Integer>();
        int l = 0, r = 0;
        while(r < nums.length){
            while(q.size()>0 && nums[r] > nums[q.peekLast()]){
                q.pollLast();
            }
            q.add(r);
            if(l > q.peek()){
                q.poll();
            }
            if(r + 1 >= k){
                l++;
                output.add(nums[q.peek()]);
            }
            r++;
        }
        return output.stream().mapToInt(i -> i).toArray();
        
    }
}