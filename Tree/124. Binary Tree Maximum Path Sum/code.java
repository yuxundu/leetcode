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
 class Res{
     public int val;
 }
class Solution {
    public int maxPathSum(TreeNode root) {
        Res res = new Res();
        res.val = root.val;
        maxSubPathSum(root,res);
        return res.val;
    }

    public int maxSubPathSum(TreeNode node, Res res){
        if(node == null) return  0;
        int leftSum = maxSubPathSum(node.left,res);
        int rightSum = maxSubPathSum(node.right,res);

        int returnSum = Math.max(leftSum+node.val,rightSum+node.val);
        returnSum = Math.max(node.val,returnSum);
        res.val = Math.max(res.val,returnSum);
        res.val = Math.max(res.val,leftSum+node.val+rightSum);
        return returnSum;
    }


}