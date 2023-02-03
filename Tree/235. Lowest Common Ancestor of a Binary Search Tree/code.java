/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        List<TreeNode> pathP = new ArrayList<>();
        findTreeNode(root,p, pathP);

        List<TreeNode> pathQ = new ArrayList<>();
        findTreeNode(root,q, pathQ);

        TreeNode ans = null;
        for(int i = 0; i < Math.min(pathP.size(),pathQ.size()); i++){
            if(pathP.get(i).val != pathQ.get(i).val){
                break;
            }
            ans = pathP.get(i);
        }

        return ans;
    }

    public boolean findTreeNode(TreeNode root, TreeNode target,List<TreeNode> path){

        path.add(root);
        
        if(root.val == target.val) return true;
        if(root.left!=null && target.val < root.val && findTreeNode(root.left, target, path)){
            return true;
        }

        if(root.right !=null && target.val > root.val &&  findTreeNode(root.right, target,path)){
            return true;
        }
        path.remove(path.size()-1);
        return false;
  
    }
}