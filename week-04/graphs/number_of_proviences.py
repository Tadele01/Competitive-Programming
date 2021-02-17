from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province, visited = 0, set()
        for i in range(len(isConnected)):
            if i not in visited:
                self.dfs(isConnected, i, visited)
                province += 1
        return province
    
    def dfs(self, graph, start, visited):
        visited.add(start)
        for neighbour in range(len(graph[start])):
            if graph[start][neighbour] == 1 and neighbour not in visited:
                self.dfs(graph, neighbour, visited)
            