/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        Map<Node,Node> oldToNew = new HashMap<>();
        return node==null?null:dfs(node,oldToNew);
        
    }

    public Node dfs(Node oldNode,Map<Node,Node> oldToNew ){
        if(oldToNew.containsKey(oldNode)) return oldToNew.get(oldNode);
        Node newNode = new Node(oldNode.val);
        oldToNew.put(oldNode,newNode);
        for(Node neighbor : oldNode.neighbors){
            newNode.neighbors.add(dfs(neighbor,oldToNew));
        }
        return newNode;
    }
}