from collections import defaultdict
from typing import List
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for pc1, pc2 in connections:
            graph[pc1].append(pc2)
            graph[pc2].append(pc1)
        
        redundant, visited, components = 0, set(), 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                pc_cnt, edge_cnt = set([i]), set()
                self.dfs(i, graph, visited, pc_cnt, edge_cnt)
                redundant += len(edge_cnt) - (len(pc_cnt) - 1)
                components += 1
        
        return -1 if redundant < components-1 else components-1

    def dfs(self, pc, graph, visited, pc_cnt, edge_cnt):
        for connection in graph[pc]:
            edge = tuple(sorted([pc, connection]))
            if edge not in edge_cnt:
                visited.add(connection)
                edge_cnt.add(edge)
                pc_cnt.add(connection)
                self.dfs(connection, graph, visited, pc_cnt, edge_cnt)
                


        
            