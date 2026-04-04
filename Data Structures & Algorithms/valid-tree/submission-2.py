class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # what is a valid tree
        # no cycle again?
        # but this time undirected...
        # honestly we need to check from every start no?
        if len(edges) < 1:
            return True
        adj = {}
        for e in edges:
            if e[0] == e[1]:
                return False
            adj[e[0]] = adj.get(e[0], set()) | {e[1]}
            adj[e[1]] = adj.get(e[1], set()) | {e[0]}
        
        visited = set()
        visiting = set()
        def cycle(start):
            print("current ajd", start, adj)
            if start in visited:
                print("already visisted and no cycles", start)
                return False
            if start in visiting:
                print("cycle detected", start)
                return True
            # end?
            if start not in adj or len(adj[start]) == 0:
                print("reached end, no cycle", start)
                visited.add(start)
                return False
            visiting.add(start)
            for nei in adj[start]:
                # remove taken edge
                adj[start].remove(nei)
                adj[nei].remove(start)
                print("took edge", start, nei)
                if cycle(nei):
                    return True
                adj[nei].add(start)
                adj[start].add(nei)
            visiting.remove(start)
            visited.add(start)
            print("fully visited", start)
            return False
        cycles = cycle(edges[0][0])
        print("cycles outputed ", cycles, visited)
        return len(visited) == n if not cycles else False
            

        