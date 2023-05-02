class Solution {
    public void rotate(int[][] matrix) {

        int left = 0, right = matrix.length-1;
        while(left < right){
            int top = left, bottom = right;
            for(int i = 0; i < (right - left); i++){
                int temp = matrix[top+i][left];
                 matrix[top+i][left] = matrix[bottom][left+i];
                 matrix[bottom][left+i] = matrix[bottom-i][right];
                 matrix[bottom-i][right] = matrix[top][right-i];
                 matrix[top][right-i] = temp;
            }
            left++;
            right--;

        }
        
    }
}