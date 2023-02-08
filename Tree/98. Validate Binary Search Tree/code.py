# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.checkRange(root,None,None)

    def checkRange(self,current,min,max):
        if not current:
            return True
        if min and current.val <= min:
            return False
        if max and current.val >= max:
            return False
        if current.left and current.val <= current.left.val:
            return False
        if current.right and current.val >= current.right.val:
            return False
        return self.checkRange(current.left,min,current.val) and self.checkRange(current.right,current.val,max)

    