"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # from copied node to source random
        rand = {}
        # from equivalent source to copy
        copy_map = {}
        current_copy = Node(head.val)
        head_copy = current_copy
        current_source = head
        # first pass
        while current_source != None:
            # get the next source node and copy it
            next_source = current_source.next
            next_copy = Node(next_source.val) if next_source else None
            # keep track of source to new copy
            copy_map[current_source] = current_copy
            # keep track of source random
            rand[current_copy] = current_source.random
            # make the current copy point to the next copy
            current_copy.next = next_copy
            # update the current copy
            current_copy = next_copy
            current_source = next_source

        print("source to copy")  
        print([(copy.val if copy else None, source.val if source else None) for copy, source in copy_map.items()])
        print("copy to source rand")
        print([(copy.val if copy else None, source.val if source else None) for copy, source in rand.items()])
        # second pass
        current_copy = head_copy
        while current_copy != None:
            if rand[current_copy] != None:
                current_copy.random = copy_map[rand[current_copy]]
            else:
                current_copy.random = None
            current_copy = current_copy.next

        return head_copy
        


 



