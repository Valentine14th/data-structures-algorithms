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
        length = 0
        curr = head
        while curr is not None:
            curr = curr.next
            length += 1
        if length == 1:
            return
        # find middle node
        # infinite loop to check
        pos = 0
        curr = head
        print(length//2)
        while pos < (length // 2) - 1:
            curr = curr.next
            pos += 1
        print(pos, curr.val)
        last = curr
        curr = curr.next
        mid = curr
        last.next = None
        # reverse second half of list
        prev = None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # now merge both lists
        curr_left = head
        curr_right = prev
        while curr_left is not None:
            temp_left = curr_left.next
            temp_right = curr_right.next
            curr_left.next = curr_right
            if temp_left:
                curr_right.next = temp_left
            curr_left = temp_left
            curr_right = temp_right







        