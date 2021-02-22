from collections import defaultdict
from collections import deque
def bfs(n, m, edges, s):
    adj_list, visited, edge_weight = defaultdict(set), set(), 6
    for edge in edges:
        adj_list[edge[0]].add(edge[1])
        adj_list[edge[1]].add(edge[0])
    result = [-1] * n
    queue = deque([(s, 0)])
    visited.add(s)
    while queue:
        cur_node, dist = queue.popleft()
        for neighbour in adj_list[cur_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                result[neighbour-1]  = dist + edge_weight
                queue.append((neighbour, dist+edge_weight))
    result.pop(s-1)
    return result