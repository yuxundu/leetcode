class TrieNode{
    boolean isWord;
    int refers = 0;
    Map<Character, TrieNode> children;

    public TrieNode(){
        isWord = false;
        children = new HashMap<>();
    }

    public void insert(String word, int index){
        refers += 1;
        if(index == word.length()){
            isWord = true;
            return;
        }

        char c = word.charAt(index);
        if(!children.containsKey(c)){
            children.put(c,new TrieNode());
        }
        children.get(c).insert(word,index + 1);
    }

    public void remove(String word, int index){
        refers -= 1;
        if(index == word.length()){
            isWord = false;
            return;
        }
        children.get(word.charAt(index)).remove(word,index + 1);
    }
}

class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        TrieNode root = new TrieNode();
        for(String word : words){
            root.insert(word,0);
        }
        List<String> ans = new ArrayList<>();
        for(int m = 0; m < board.length; m++){
            for(int n = 0; n < board[0].length; n++){
                dfs(board,m,n,ans,"",root,root);
            }
        }
        return ans; 
    }

    public void dfs(char[][] board, int x, int y, List<String> ans, String str, TrieNode node, TrieNode root){
        if( x < 0  || x >= board.length || y < 0 || y >= board[0].length) return;
        char c = board[x][y];
        if('*' == c|| node.refers < 1 || !node.children.containsKey(c)) return;

        board[x][y] = '*';
        str = str + c;
        TrieNode childNode = node.children.get(c);
        if(childNode.isWord){
            ans.add(str);
            root.remove(str,0);
        }
        dfs(board,x+1,y,ans,str,childNode,root);
        dfs(board,x-1,y,ans,str,childNode,root);
        dfs(board,x,y+1,ans,str,childNode,root);
        dfs(board,x,y-1,ans,str,childNode,root);
        board[x][y] = c;
    }
}