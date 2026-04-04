class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # not possible if cycle
        # adjacency list graph
        graph = {}
        for p in prerequisites:
            graph[p[0]] = graph.get(p[0], set()) | {p[1]}
        print(graph)
        # dfs 
        seen = set()
        allseen = set()
        
        def no_cycle(node):
            if node in allseen:
                return True
            if node in seen:
                print("seen cycle", node, seen)
                return False
            print("adding", node)
            seen.add(node)
            for n in graph.get(node, []):
                if not no_cycle(n):
                    return False
                print("removing", n)
            seen.remove(node)
            allseen.add(node)
            return True

        for c in graph.keys():
            if c in allseen:
                print("seen before skip", c)
                continue
            print("starting from ", c)
            if not no_cycle(c):
                print("cycle found from ", c)
                return False
        return True

                

        

        