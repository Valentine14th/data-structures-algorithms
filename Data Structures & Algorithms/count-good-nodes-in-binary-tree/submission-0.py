# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # if parent is good, then all before are smaller
        # so if greater than parent, then also good
        # if parent is not good, then there are some bigger
        # if child > parent, but there were some bigger before
        # we only need to check until the next good node
        # we need to keep track of the last seen good node in the path
        # everything in between is smaller
        def rec(curr, lastgood):
            if not curr:
                return 0
            if curr.val >= lastgood:
                print("good", curr.val)
                return 1 + rec(curr.left, curr.val) + rec(curr.right, curr.val)
            else:
                return rec(curr.left, lastgood) + rec(curr.right, lastgood)
        return rec(root, root.val)
        

        