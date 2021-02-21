from typing import List
class solution:
    def max_area_of_island(grid:List[List[int]])->int:
        num_row, num_col, max_area, visited = len(grid), len(grid[0]), [0], set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for row in range(num_row):
            for col in range(num_col):
                if grid[row][col] == 1:
                    area = self.dfs(grid, visited, directions, (row, col), num_row, num_col, 0, max_area)
        return max_area[0]
    def dfs(grid, visited, directions, pos, num_row, num_col, area, max_area):
        area +=1 
        visited.add(pos)
        for direction in directions:
            new_r, new_c = pos[0] + direction[0], pos[1] + direction[1]
            if 0<= new_r < num_row and 0<= new_c < num_col and (new_r, new_c) not in visited and  \
                    grid[new_r][new_c] == 1:
                area = self.dfs(grid, visited, directions, (new_r, new_c), num_row, num_col, area, max_area)
        max_area[0] = max(area, max_area[0])
        return area