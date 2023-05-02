class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> res = new ArrayList<>();

        boolean merge = true;
        
        for(int i = 0; i < intervals.length; i++){

            if(!merge){

                res.add(intervals[i]);
            }
            else if(newInterval[1] < intervals[i][0]){

                res.add(newInterval);
                res.add(intervals[i]);
                merge = false;
            }
            else if(newInterval[0] > intervals[i][1]){

                res.add(intervals[i]);
            }
            else{

                int x = Math.min(newInterval[0],intervals[i][0]);
                int y = Math.max(newInterval[1],intervals[i][1]);
                newInterval[0] = x;
                newInterval[1] = y;

            }
        }

        if(merge){
            res.add(newInterval);
        }
        
        int[][] ans  =  new int[res.size()][];
        for(int i = 0; i < res.size(); i++){
            ans[i] = res.get(i);
        }
        return ans;
        
    }
}