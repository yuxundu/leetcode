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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if(preorder.length == 0 ) return null;

        TreeNode currentNode = new TreeNode();
        currentNode.val = preorder[0];

        int currIndex = -1;


        for(int i = 0; i < inorder.length; i++){
            if(currentNode.val == inorder[i]){
                currIndex = i;
                break;
            }
        }

        int[] leftInorder = Arrays.copyOfRange(inorder, 0, currIndex);
        int[] leftPreorder = Arrays.copyOfRange(preorder, 1, 1+leftInorder.length);
        currentNode.left = buildTree(leftPreorder,leftInorder);
        int[] rightInorder = Arrays.copyOfRange(inorder, currIndex+1, inorder.length);
        int[] rightPreorder = Arrays.copyOfRange(preorder, 1+leftInorder.length, preorder.length);
        currentNode.right = buildTree(rightPreorder,rightInorder);
        return currentNode;


        
    }
}