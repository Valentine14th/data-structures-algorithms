# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        out = [[root.val]]
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if len(level) > 0:
                out.append([n.val for n in level])
                queue.extend(level)
        return out

        