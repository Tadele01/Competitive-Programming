from collections import defaultdict
from collections import deque
from heapq import heappop, heappush, heapify
def bfs(n, m, edges, s):
    adj_list, visited, edge_weight = defaultdict(set), set(), 6
    for edge in edges:
        adj_list[edge[0]].add(edge[1])
        adj_list[edge[1]].add(edge[0])
    distances = defaultdict(tuple)
    for i in range(1, n+1):
        if i ==s :
            continue
        distances[i] = (i, 0)
    queue = deque([(s, 0)])
    visited.add(s)
    while queue:
        cur_node, dist = queue.popleft()
        for neighbour in adj_list[cur_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                distances[neighbour]  = (neighbour, dist + edge_weight)
                queue.append((neighbour, dist+edge_weight))
    min_heap = []
    for key, value in distances.items():
        if value[1] == 0:
            value = (value[0], -1)
        heappush(min_heap, value)
    return [heappop(min_heap)[1] for i in range(len(min_heap))]
