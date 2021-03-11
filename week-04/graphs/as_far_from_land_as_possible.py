from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue, visited = deque(), set()
        num_row, num_col = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        max_dist = 0
        for row in range(num_row):
            for col in range(num_col):
                if grid[row][col] == 1:
                    queue.append((row, col, 0))
        if len(queue) == (num_row*num_col) or len(queue) == 0:
            return -1
        while queue:
            row, col, dist = queue.popleft()
            max_dist = max(max_dist, dist)
            visited.add((row, col))
            for direction in directions:
                new_r, new_c = row+direction[0], col+direction[1]
                if self.is_valid(new_r, new_c, grid, visited):
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c, dist+1))
        return max_dist
    def is_valid(self, new_r, new_c, grid, visited):
        num_row, num_col = len(grid), len(grid[0])
        if 0<= new_r < num_row and 0<= new_c < num_col and (new_r, new_c) not in                        visited:
            return True
        return False
        
        
        