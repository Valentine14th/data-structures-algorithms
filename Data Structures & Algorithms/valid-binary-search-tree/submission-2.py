# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(root: Optional[TreeNode], maxi: int, mini: int):
            if root is None:
                return True
            if not (maxi < root.val < mini):
                return False
            return valid(root.left, maxi, root.val) and valid(root.right, root.val, mini)
            
        
        return valid(root, float("-inf"), float("inf"))
        
        