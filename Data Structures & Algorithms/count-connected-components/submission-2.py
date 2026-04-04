class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        u = UnionFind(n)
        for e in edges:
            u.union(e[0], e[1])
        print(u.parents)
        u.flatten()
        return len(set(u.parents))
        

        

class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [1]*n

    def flatten(self):
        for i in range(len(self.parents)):
            self.find(i)

    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.ranks[px] < self.ranks[py]:
            self.parents[px] = py
            self.ranks[py] += self.ranks[px]
        elif self.ranks[px] >= self.ranks[py]:
            self.parents[py] = px
            self.ranks[px] += self.ranks[py]
        return True

        