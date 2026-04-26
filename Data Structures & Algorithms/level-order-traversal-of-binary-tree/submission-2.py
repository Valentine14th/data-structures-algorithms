# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        out = []
        q.append(root)
        while q:
            print([n.val for n in q])
            l = len(q)
            out.append([n.val for n in q])
            popped = 0
            while popped < l:
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                popped += 1
        return out

        