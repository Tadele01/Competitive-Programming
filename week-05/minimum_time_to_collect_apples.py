from collections import deque, defaultdict
from typing import List
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj_list, queue, visited = defaultdict(list), deque(), set()
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        if not adj_list:
            return 0
        n = len(adj_list)
        dist, prev = [-1 for i in range(n)], [-1 for i in range(n)]
        queue.append(0)
        visited.add(0)
        dist[0], prev[0] = 0, 0
        while queue:
            cur_vertex = queue.popleft()
            for neighbour in adj_list[cur_vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                    dist[neighbour] = dist[cur_vertex] +1 
                    prev[neighbour] = cur_vertex
        unique_edge = set()
        for i in range(len(dist)):
            if hasApple[i]:
                tmp = i
                while tmp != 0:
                    edge = (tmp, prev[tmp])
                    tmp = prev[tmp]
                    unique_edge.add(edge)
        return 2 * len(unique_edge) #since all edges are undirected we multiply by 2