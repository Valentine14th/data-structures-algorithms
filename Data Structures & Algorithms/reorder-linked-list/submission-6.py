# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        # find middle
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None
        # reverse second half of list
        prev = None
        curr = mid
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # now merge both lists
        curr_left = head
        curr_right = prev
        while curr_right is not None:
            temp_left = curr_left.next
            temp_right = curr_right.next
            curr_left.next = curr_right
            if temp_left:
                curr_right.next = temp_left
            curr_left = temp_left
            curr_right = temp_right







        