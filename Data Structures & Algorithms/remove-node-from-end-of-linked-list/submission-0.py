# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def dfs(node: Optional[ListNode]) -> int:
            if node == None:
                return 1
            else:
                current = dfs(node.next)
                print(f"current node {current} has value {node.val}")
                if current == n+1:
                    node.next = node.next.next
                return current + 1

        start = ListNode(next=head)
        dfs(start)
        return start.next
                    


        