from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, queue, tot_min = set(), deque(), 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        num_row, num_col = len(grid), len(grid[0])
        for row in range(num_row):
            for col in range(num_col):
                if grid[row][col] == 2:
                    queue.append(((row, col), 0))
                elif grid[row][col] == 1:
                    fresh.add((row, col))
        while queue:
            size = len(queue)
            for i in range(size):
                pos, minutes = queue.popleft()
                tot_min = max(minutes, tot_min)
                for direction in directions:
                    new_r, new_c = pos[0] + direction[0],                                       pos[1]+direction[1]
                    if self.is_valid(grid, new_r, new_c):
                        fresh.remove((new_r, new_c))
                        grid[new_r][new_c] = 2
                        queue.append(((new_r, new_c), minutes+1))
        if fresh:
            return -1
        return tot_min
    def is_valid(self, grid, new_r, new_c):               
        num_row, num_col = len(grid), len(grid[0])
        if 0<= new_r < num_row and 0<= new_c < num_col and grid[new_r]                  [new_c] == 1:
            return True
        return False
            