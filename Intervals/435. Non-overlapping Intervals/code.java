class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals,new java.util.Comparator<int[]>(){
            public int compare(int[] a, int[] b){
                if(a[0] == b[0]) {

                    return Integer.compare(a[1],b[1]);
                }
                return Integer.compare(a[0],b[0]);
            }
        });

        int count = 0;
        int[] output = intervals[0];
        
        for(int i = 1; i < intervals.length; i++){

            if(output[1] > intervals[i][0]){

                if(output[1] > intervals[i][1]){
                    output = intervals[i];
                }
                 count++;
            }
            else{

                output = intervals[i];
               
            }

        }

        return count;
        
    }
}