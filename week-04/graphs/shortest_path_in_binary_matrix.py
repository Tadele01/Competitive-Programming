from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue, visited = deque(()), set()
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        num_row, num_col = len(grid), len(grid[0])
        if grid[0][0] != 0 or grid[num_row-1][num_col-1] != 0:
            return -1
        clear_path = 0
        queue.append((0, 0, 1))
        visited.add((0,0))
        while queue:
            row, col, dist = queue.popleft()
            clear_path = max(clear_path, dist)
            if row == num_row-1 and col == num_col-1:
                break
            for direction in directions:
                new_r, new_c = row + direction[0], col + direction[1]
                if self.is_valid(new_r, new_c, grid, visited):
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c, dist+1))
        return clear_path if (num_row-1, num_col-1) in visited else -1
    def is_valid(self, new_r, new_c, grid, visited):
        num_row, num_col = len(grid), len(grid[0])
        if 0<= new_r < num_row and 0<= new_c < num_col and (new_r, new_c) not in visited                and grid[new_r][new_c] == 0:
            return True
        return False
            
        