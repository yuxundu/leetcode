class Solution {
    public boolean isValidSudoku(char[][] board) {
        List<Set<Character>> rowList = new ArrayList<>();
        for(int i=0; i<9; i++){
            rowList.add(new HashSet<Character>());
        }

        List<Set<Character>> columnList = new ArrayList<>();
        for(int i=0; i<9; i++){
            columnList.add(new HashSet<Character>());
        }

        List<Set<Character>> subBoxList = new ArrayList<>();
        for(int i=0; i<9; i++){
            subBoxList.add(new HashSet<Character>());
        }
 
        for(int i=0; i < board.length; i++){
            for(int j=0; j < board[0].length; j++){
                if(board[i][j] == '.'){
                    continue;
                }
                int index = j/3 + 3*(i/3);
                if(rowList.get(i).contains(board[i][j])){
                    return false;
                }
                if(columnList.get(j).contains(board[i][j])){
                    return false;
                }
                if(subBoxList.get(index).contains(board[i][j])){
                    return false;
                }
                rowList.get(i).add(board[i][j]);
                columnList.get(j).add(board[i][j]);
                subBoxList.get(index).add(board[i][j]);
            }
        }
        return true;
        
    }
}