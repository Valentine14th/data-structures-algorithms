# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder index[0] is the root
        # if we find it in inorder, we can split left and right
        # preorder 1,2,3,4
        # inorder 2,1,3,4
        # [1,2,3,4,5,null,6]
        # preorder [1,2,4,5,3,6]
        # inorder  [4,2,5,1,3,6]
        ri = -1
        def rec(i, j):
            nonlocal ri
            if i >= j:
                print("abort", i ,j)
                return
            ri += 1
            r = preorder[ri]
            print(ri, r, i ,j)
            mid = i+inorder[i:j].index(r)
            n = TreeNode(r)
            n.left = rec(i, mid)
            n.right = rec(mid+1, j)
            return n
        return rec(0, len(preorder))



        