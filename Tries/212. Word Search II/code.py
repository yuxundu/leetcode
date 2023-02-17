class TrieNode:
    def __init__(self):
        self.isWord = False
        self.refers = 0
        self.children = [None] * 26

    def insert(self, word:str, index:int):
        self.refers = self.refers + 1
        if index == len(word):
            self.isWord = True
            return
        p = ord(word[index]) - ord("a")
        if not self.children[p]:
            self.children[p] = TrieNode()
        self.children[p].insert(word, index + 1)
    
    def remove(self, word:str, index:int):
        self.refers = self.refers - 1
        if index == len(word):
            self.isWord = False
            return
        p = ord(word[index]) - ord('a')
        self.children[p].remove(word, index + 1)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        ans = []
        for word in words:
            root.insert(word,0)
        for m in range(len(board)):
            for n in range(len(board[0])):
                self.dfs(board, m, n, root, root,ans,"")
        return ans

    def dfs(self,board: List[List[str]], m: int, n: int, node:TrieNode, root:TrieNode,ans:  List[str],word:str):
        if m < 0 or n < 0 or m >= len(board) or n >= len(board[0]):
            return
        if "*" == board[m][n]:
            return
        p = ord(board[m][n]) - ord('a')
        if not node.children[p]:
            return
        if node.children[p].refers < 1:
            return

        c = board[m][n]
        word += c
        board[m][n] = "*"
        node = node.children[p]
        if node.isWord:
            print(word)
            ans.append(word)
            root.remove(word,0)
        self.dfs(board, m+1, n, node, root,ans,word)
        self.dfs(board, m-1, n, node, root,ans,word)
        self.dfs(board, m, n+1, node, root,ans,word)
        self.dfs(board, m, n-1, node, root,ans,word)
        board[m][n] = c








        
    