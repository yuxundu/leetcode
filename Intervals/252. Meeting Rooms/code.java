class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        if(intervals.length == 0) return true;;
        Arrays.sort(intervals, new java.util.Comparator<int[]>(){
            public int compare(int[] a, int[] b){
                if(a[0] == b[0]){
                    return Integer.compare(a[1],b[1]);
                }
                return Integer.compare(a[0], b[0]);
            }
        });
        int preEnd = intervals[0][1];
        for(int i = 1; i < intervals.length; i++){
            if(intervals[i][0] < preEnd){
                return false; 
            }
            preEnd = intervals[i][1];

        }

         return true;
        
    }
}