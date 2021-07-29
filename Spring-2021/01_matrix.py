from collections import deque
from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        cache = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    mat[i][j] = self.bfs(i, j, mat)
        
        return mat
    
    def bfs(self, i, j, mat):        
        queue, visited = deque([(i, j, 0)]), set()
        while queue:
            for i in range(len(queue)):
                x, y, d = queue.popleft()
                if mat[x][y] == 0:
                    return d
                for n, m in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    r, c = x+n, y+m
                    if 0 <= r < len(mat) and 0 <= c < len(mat[0]) and (r, c) not in visited:
                        visited.add((r, c))
                        queue.append((r, c, d+1))