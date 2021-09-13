from collections import defaultdict
from heapq import heappop, heappush
class Solution(object):
    def reachableNodes(self, edges, M, N):
        graph = defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        pq, dist, used, ans = [(0, 0)], {0: 0}, {}, 0

        while pq:
            d, node = heappop(pq)
            if d > dist[node]: continue
            ans += 1
            for nei, weight in graph[node].items():
                v = min(weight, M - d)
                used[node, nei] = v
                d2 = d + weight + 1
                if d2 < dist.get(nei, M+1):
                    heappush(pq, (d2, nei))
                    dist[nei] = d2

        for u, v, w in edges:
            ans += min(w, used.get((u, v), 0) + used.get((v, u), 0))

        return ans