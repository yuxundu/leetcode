# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        pre = slow.next= None
        while second:
            temp = second.next
            second.next = pre
            pre = second
            second = temp

        first,second = head,pre
        while second:
            temp1,temp2 = first.next,second.next
            first.next = second
            second.next = temp1
            second = temp2
            first = temp1
            
            





