# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergeList = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None
                mergeList.append(self.mergeList(l1,l2))
            lists = mergeList
        return lists[0]



    def mergeList(self, first: Optional[ListNode], second: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while first and second:
            if first.val < second.val:
                tail.next = first
                first = first.next
            else:
                tail.next = second
                second = second.next
            tail = tail.next
        if first:
            tail.next = first
        if second:
            tail.next = second
        return dummy.next

        