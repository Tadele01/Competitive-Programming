from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, -1)]
        num_row, num_col = len(grid), len(grid[0])
        for row in range(num_row):
            for col in range(num_col):
                moves = []
                for direction in directions:
                    new_r, new_c = row + direction[0], col + direction[1]
                    if self.is_valid(new_r, new_c, grid):
                        moves.append(grid[new_r][new_c])
                if moves:
                    val = min(moves)
                    grid[row][col] += val

        return grid[num_row-1][num_col-1]
    
    def is_valid(self, new_r, new_c, grid):
        if 0<= new_r < len(grid) and 0 <= new_c < len(grid[0]):
            return True
        return False