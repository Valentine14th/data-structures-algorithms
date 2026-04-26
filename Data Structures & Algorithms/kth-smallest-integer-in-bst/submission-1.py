# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # if more less than k left of root, then right
        steps = 0
        result = 0
        def rec(curr):
            nonlocal steps
            nonlocal result
            if not curr:
                return 
            rec(curr.left)
            steps += 1
            if steps == k:
                result = curr.val
                return
            rec(curr.right)
        rec(root)
        return result

        