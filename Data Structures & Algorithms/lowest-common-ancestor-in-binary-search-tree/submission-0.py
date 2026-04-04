# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def findval(val: int) -> List[bool]:
            out = []
            current = root
            while val != current.val:
                if val < current.val:
                    current = current.left
                    out.append(False)
                else:
                    current = current.right
                    out.append(True)
            return out
        
        outp = findval(p.val)
        outq = findval(q.val)
        i = 0
        current = root
        print("left", outp)
        print("right", outq)
        while len(outp) > i and len(outq) > i and outp[i] == outq[i]:
            if outp[i]:
                current = current.right
            else:
                current = current.left
            i += 1
        return current


        