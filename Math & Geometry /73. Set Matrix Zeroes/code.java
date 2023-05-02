class Solution {
    public void setZeroes(int[][] matrix) {
         int row = matrix.length;
         int column = matrix[0].length;
         int rowZero = 1;

         for(int i = 0; i < row; i++){
             for(int j = 0; j < column; j++){
                 if(matrix[i][j] == 0){
                    matrix[0][j] = 0;
                    if(i > 0){
                        matrix[i][0] = 0;
                    }
                    else{
                        rowZero = 0;
                    }
                 }
             }
         }

         for(int i = 1; i < row; i++){
             for(int j = 1; j < column; j++){
                 if(matrix[0][j] == 0 || matrix[i][0] == 0){
                     matrix[i][j] = 0;
                 }
             }

         }
         if(matrix[0][0] == 0){
             for(int i = 0; i < row; i++){
                 matrix[i][0] = 0;
             }
         }
         if(rowZero == 0){
             for(int i = 0; i < column; i++){
                 matrix[0][i] = 0;
             }
         }
    }
}