"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        map = {None:None}
        while current:
            node = Node(current.val)
            map[current] = node
            current =current.next

        current = head
        while current:
            
            map[current].next = map[current.next]
            
            map[current].random = map[current.random]
            current = current.next
        return map[head] if head else None