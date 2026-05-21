class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((v,t))
        q = []
        dist = [float("inf")]*(n+1)
        dist[k] = 0
        heapq.heappush(q, (0,k))
        while q:
            d, node = heapq.heappop(q)
            if d > dist[node]:
                continue
            for nei, t in adj[node]:
                if dist[nei] > dist[node] + t:
                    dist[nei] = dist[node]+t
                    heapq.heappush(q, (dist[nei], nei)) 
        return max(dist[1:]) if max(dist[1:]) != float("inf") else -1
        