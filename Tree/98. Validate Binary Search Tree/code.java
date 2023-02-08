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
    public boolean isValidBST(TreeNode root) {
        return checkRange(root,null,null);
    }

    public boolean checkRange(TreeNode current, Integer min, Integer max){
        if(current == null) return true;

        if(min != null && current.val <= min) return false;
        if(max != null && current.val >= max) return false;

        if(current.left != null && current.left.val >= current.val ){
            return false;
        }

        if(current.right != null && current.right.val <= current.val ){
            return false;
        }

        return checkRange(current.left,min,current.val) && checkRange(current.right,current.val, max);
    }
}