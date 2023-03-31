# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pre,left,right = None, head, head;
        for i in range(0,n):
            left = left.next
        while left:
            left = left.next
            pre = right
            right = right.next
        if pre:
            pre.next = right.next
        else:
            head = right.next
        return head
