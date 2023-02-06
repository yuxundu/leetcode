# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def addLeft(node,stack):
            stack.append(node)
            while node.left:
                stack.append(node.left)
                node = node.left
        
        stack = []
        addLeft(root,stack)
        order = 0
        while len(stack) > 0:
            node = stack.pop()
            order += 1
            if order == k:
                return node.val
            if node.right:
                addLeft(node.right,stack)
        