class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort
        # dfs with indegree thing
        # calc indeg of all nodes
        # take node with lowest indeg (in acyclic needs to be 0)
        # add to result, and reduce in deg of all the neighbors
        # 
        adj = defaultdict(list)
        ins = defaultdict(int)
        for c1, c2 in prerequisites:
            adj[c2].append(c1)
            ins[c1] += 1
        q = deque()
        out = []
        for n in range(numCourses):
            if ins[n] == 0:
                q.append(n)
        while q:
            n = q.popleft()
            out.append(n)
            for nei in adj[n]:
                ins[nei] -= 1
                if ins[nei] == 0:
                    q.append(nei)
        return out if len(out) == numCourses else []
        
        