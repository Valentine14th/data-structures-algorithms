class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        out = []
        adj = defaultdict(list)
        for c1, c2 in prerequisites:
            adj[c2].append(c1)
        visited = set()
        visiting = set()
        def dfs(n):
            if n in visiting:
                return False
            if n in visited:
                return True
            visiting.add(n)
            for nei in adj[n]:
                if not dfs(nei):
                    return False
            out.append(n)
            visited.add(n)
            visiting.remove(n)
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return []
        return out[::-1]





        