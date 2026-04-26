# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(curr):
            if curr is None:
                return None
            elif curr.val == p.val or curr.val == q.val:
                return curr
            left = dfs(curr.left)
            right = dfs(curr.right)
            if left and right:
                return curr
            return right or left
        return dfs(root)
        