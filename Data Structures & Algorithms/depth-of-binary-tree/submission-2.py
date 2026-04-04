# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        maxlen = 0
        stack.append((root, 1))
        if not root:
            return 0
        while stack:
            n, d = stack.pop()
            maxlen = max(maxlen,d)
            if n.left:
                stack.append((n.left, d+1))
            if n.right:
                stack.append((n.right, d+1))
        return maxlen

        