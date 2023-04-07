"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def dfs(oldNode:'Node'):
            if oldNode in oldToNew:
                return oldToNew[oldNode]
            newNode = Node(oldNode.val)
            oldToNew[oldNode] = newNode
            for neighbor in oldNode.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            return newNode

        return dfs(node) if node else None
