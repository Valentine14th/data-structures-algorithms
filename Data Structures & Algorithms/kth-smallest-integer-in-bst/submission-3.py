# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        steps = 0
        stack = []
        while curr is not None or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            steps += 1
            if steps == k:
                return curr.val
            curr = curr.right
            


        