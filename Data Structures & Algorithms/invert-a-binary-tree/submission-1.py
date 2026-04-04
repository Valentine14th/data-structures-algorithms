# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        if root != None:
            if root.left and root.right:
                temp = root.left
                root.left = root.right
                root.right = temp
            elif root.left and not root.right:
                root.right = root.left
                root.left = None
            elif root.right and not root.left:
                root.left = root.right
                root.right = None
            self.invertTree(root.left)
            self.invertTree(root.right)
        
        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            dfs(root.right)
            print(root.val)

        def bfs(root):
            q = deque()
            q.append(root)
            while q:
                print([n.val for n in q])
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return root

        