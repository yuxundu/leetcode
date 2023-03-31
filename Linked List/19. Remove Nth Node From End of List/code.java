/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode right = head, left = head, pre = null;
        for(int i = 0; i < n; i++){
            right = right.next;
        }
        while(right != null){
            right = right.next;
            pre = left;
            left = left.next;
        }
        if(pre != null){
            pre.next = left.next;
        }
        else{
            head = left.next;
        }
        return head;
    }
}