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
    public boolean hasCycle(ListNode head) {
        ListNode one = head;
        ListNode two = head;
        while(two != null && two.next != null){
            one = one.next;
            two = two.next.next;
            if(one == two){
                return true;
            }
        }
        return false;
        
    }
}
