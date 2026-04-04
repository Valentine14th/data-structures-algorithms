"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        seen = set()
        cloned = {1: Node(1)}
        def bfs():
            queueo = deque()
            queueo.append(node)
            while len(queueo) > 0:
                curro = queueo.popleft()
                if curro.val not in cloned:
                    print("new copy", curro.val)
                    cloned[curro.val] = Node(curro.val)
                currc = cloned[curro.val] 
                seen.add(curro.val)
                print("seen", curro.val)
                neigh = []
                for n in curro.neighbors:
                    if n.val not in cloned:
                        print("new copy v2", n.val)
                        cloned[n.val] = Node(n.val)
                    clone = cloned[n.val]
                    neigh.append(clone)
                    if n.val not in seen:
                        queueo.append(n)
                currc.neighbors = neigh
                print("neighbors", currc.val, currc, neigh)
                
        bfs()
        return cloned[1]

            
            
                    
        