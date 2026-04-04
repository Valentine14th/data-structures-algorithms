# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return
        current = head
        length = 1
        # find out length
        while current.next != None:
            current = current.next
            length += 1
        print("length", length)
        mid = head
        midi = math.ceil(length//2)
        # get to middle node
        for i in range(midi):
            mid = mid.next
        # reverse from middle node
        prev = None
        curr = mid
        for i in range(midi, length):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # build from two halves
        print("revhead", prev.val, prev.next.val)
        revhead = prev
        revcurr = revhead
        norcurr = head
        out = ListNode(0)
        outcurr = out
        for i in range(midi):
            outcurr.next = norcurr
            outcurr = outcurr.next
            norcurr = norcurr.next
            outcurr.next = revcurr
            revcurr = revcurr.next
            outcurr = outcurr.next
        head.next = out.next.next

