# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if  both are null
        if not subRoot and not root:
            return True
        # if one is null but not the other
        elif not root or not subRoot:
            return False
        # if both are defined and equal
        elif root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right) or (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        # if both are defined but different
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root, subRoot):
        # if  both are null
        if not subRoot and not root:
            return True
        # if one is null but not the other
        elif not root or not subRoot:
            return False
        # if both are defined and equal
        elif root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right) 
        # if both are define but different
        else:
            return False
        
        
        