import java.util.Comparator;
class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, new Comparator<int[]>(){
            public int compare(int[] a, int[] b){
                return Integer.compare(a[0],b[0]);
            }
        });
        List<int[]> output = new ArrayList<>();
        output.add(intervals[0]);
        for(int i = 0; i < intervals.length; i++){
            int[] last = output.get(output.size()-1);
            if(intervals[i][0] <= last[1]){
                last[1] = Math.max(intervals[i][1], last[1]);
            }
            else{
                output.add(intervals[i]);
            }
        }

        int[][] ans = new int[output.size()][];

        for(int i = 0; i < output.size();i++){
            ans[i] = output.get(i);
        }
        return ans;

    }
}