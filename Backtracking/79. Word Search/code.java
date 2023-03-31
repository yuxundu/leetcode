class Solution {
    public boolean exist(char[][] board, String word) {
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(travers(board,word,i,j,0)) return true;
            }
        }
        return false;
    }

    public boolean travers(char[][] board, String word, int x, int y, int i){
        if(x < 0 || y < 0 || x >= board.length || y >= board[0].length || i >= word.length() || board[x][y] != word.charAt(i) ||  board[x][y] == '*'){
            return false;
        } 
        if(i == word.length()-1) return true;
        char temp = board[x][y];
        board[x][y] = '*';
        if(travers(board,word,x-1,y,i+1)) return true;
        if(travers(board,word,x+1,y,i+1)) return true;
        if(travers(board,word,x,y-1,i+1)) return true;
        if(travers(board,word,x,y+1,i+1)) return true;
        board[x][y] = temp;
        return false;
    }
}