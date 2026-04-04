/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
        let out;
        if(list1 && list2){
            if(list1.val < list2.val){
                out = list1
                list1 = list1.next
            }
            else{
                out = list2
                list2 = list2.next
            }     
        }
        else if(list1){
            out = list1
            list1 = list1.next
        }
        else if(list2){
            out = list2
            list2 = list2.next
        }
        else{
            return null
        }
        let head = out
        while(list1 != null || list2!= null){
            if(list1 && list2){
                if(list1.val < list2.val){
                    out.next = list1
                    list1 = list1.next
                }
                else{
                    out.next = list2
                    list2 = list2.next
                }
            }
            else if(list1){
                out.next = list1
                list1 = list1.next
            }
            else{
                out.next = list2
                list2 = list2.next
            }
            out = out.next
        }
        return head
    }
}
