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
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists == null || lists.length == 0){
            return null;
        }
        List<ListNode> ansList = Arrays.asList(lists);
        while(ansList.size() > 1){
            List<ListNode> mergeList = new ArrayList<>();
            for(int i = 0; i < ansList.size(); i = i+2){
                ListNode l1 = ansList.get(i);
                ListNode l2 = (i+1) < ansList.size()?ansList.get(i+1):null;
                mergeList.add(mergeToLists(l1,l2));
            }
            ansList = mergeList;
        }
        return ansList.get(0);
    }

    public ListNode mergeToLists(ListNode first, ListNode second){
        ListNode ans = new ListNode(); 
        ListNode tail = ans;
        while(first != null && second != null){
            if(first.val < second.val){
                tail.next = first;
                first = first.next;  
            }
            else{
                tail.next = second;
                second = second.next;
            }
            tail = tail.next;

        }
        if(first!=null){
            tail.next = first;
        }
        if(second!=null){
            tail.next = second;
        }
        return ans.next;
    }
}