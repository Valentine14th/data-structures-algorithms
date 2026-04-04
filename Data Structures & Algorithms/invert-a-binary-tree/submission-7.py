# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        stack.append(root)
        if not root:
            return root
        while len(stack) > 0:
            n = stack.pop()
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)
            n.left, n.right = n.right, n.left
        return root

        