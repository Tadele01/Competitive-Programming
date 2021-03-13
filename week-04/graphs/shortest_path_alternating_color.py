from collections import defaultdict
from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        queue, visited = deque(), set()
        result = [float('inf')]*n
        red_adj_list = defaultdict(list)
        blue_adj_list = defaultdict(list)
        for value in red_edges:
            red_adj_list[value[0]].append((value[1], 'r'))
        for value in blue_edges:
            blue_adj_list[value[0]].append((value[1], 'b'))
        queue.append((0, 0, 'root'))
        visited.add((0,'root'))
        while queue:
            node, dist, color = queue.popleft()
            result[node] = min(result[node], dist)
            for neighbour in red_adj_list[node]:
                neigh, neigh_color = neighbour
                if neighbour not in visited and color != neigh_color:
                    queue.append((neigh, dist+1, neigh_color))
                    visited.add((neigh, neigh_color))
            for neighbour in blue_adj_list[node]:
                neigh, neigh_color = neighbour
                if neighbour not in visited and color != neigh_color:
                    queue.append((neigh, dist+1, neigh_color))
                    visited.add((neigh, neigh_color))
        
        result = [-1 if i == float('inf') else i for i in result]
        return result
    
        
