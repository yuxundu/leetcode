# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        res = [root.val]

        def maxSubSum(node):
            if not node:
                return 0
            leftSum = maxSubSum(node.left)
            rightSum = maxSubSum(node.right)

            returnSum = max(leftSum+node.val, rightSum+node.val,node.val)
            res[0] = max(res[0],returnSum,leftSum+node.val+rightSum)
            return returnSum

        maxSubSum(root)
        return res[0]

