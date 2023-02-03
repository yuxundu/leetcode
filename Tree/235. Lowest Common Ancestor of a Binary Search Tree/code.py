# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pathP = []
        self.findPath(root,p,pathP)
        pathQ = []
        self.findPath(root,q,pathQ)

        ans = None

        length = min(len(pathP),len(pathQ))

        for i in range(length):
            if pathP[i].val != pathQ[i].val:
                break
            ans = pathP[i]
        return ans


    def findPath(self,root,target ,path):
        path.append(root)
        if root.val == target.val:
            return True
        if root.left and target.val < root.val and self.findPath(root.left,target,path):
            return True
        if root.right and target.val > root.val and self.findPath(root.right,target,path):
            return True
        path.pop()
        return False

