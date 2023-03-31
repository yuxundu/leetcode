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
    public void reorderList(ListNode head) {
        ListNode slowNode = head;
        ListNode fastNode = head.next;
        while(fastNode!=null){
            slowNode = slowNode.next;
            for(int i = 0; i < 2 && fastNode != null; i++){
                fastNode = fastNode.next;
            }
        }
        ListNode secondHead = slowNode.next;
        slowNode.next = null;

        ListNode preNode = null;
        ListNode nextNode = null;
        while(secondHead!=null){
            nextNode = secondHead.next;
            secondHead.next = preNode;
            preNode = secondHead;
            secondHead = nextNode;
        }

        secondHead = preNode;
        ListNode currentNode = head;
        while(secondHead != null){
            nextNode = currentNode.next;
            ListNode secondtNode = new ListNode(secondHead.val);
            currentNode.next = secondtNode;
            secondtNode.next = nextNode;
            currentNode = nextNode;

            secondHead = secondHead.next;
        }

    }
}