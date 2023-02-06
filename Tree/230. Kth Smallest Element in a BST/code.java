/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stack = new Stack<>();
        int order = 0;
        addLeft(root,stack);
        while(!stack.empty()){
            TreeNode node = stack.pop();
            if(++order == k){
                return node.val;
            }
            if(node.right != null){
                addLeft(node.right,stack);
            }
        }
        return -1;
        
    }

    public void addLeft(TreeNode node,  Stack<TreeNode> stack){
        stack.push(node);
        while(node.left!=null){
            stack.push(node.left);
            node = node.left;
        }
    }
}