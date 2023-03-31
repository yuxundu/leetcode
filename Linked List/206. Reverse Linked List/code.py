# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        preP,currentP,nextP = None, head, None
        while currentP:
            nextP = currentP.next
            currentP.next = preP
            preP = currentP
            currentP = nextP
        return preP

    