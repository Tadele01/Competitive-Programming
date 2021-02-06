class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = [0]
        directions = [(0, 1), (0, -1), (-1, 0)]
        n, m = len(grid), len(grid[0])
        cur_position = (n-1, 0)
        self.count_negatives(grid, directions, n, m, cur_position, count)
        return count[0]
    def count_negatives(self, grid, directions, n, m, cur_position, count):
        if(0 <= cur_position[0] < n and 0 <= cur_position[1] < m):
            if(grid[cur_position[0]][cur_position[1]] < 0):
                remaining_negatives = m - cur_position[1]
                count[0] += remaining_negatives
                direction = directions[2]
                cur_position = (cur_position[0]+direction[0], cur_position[1] + direction[1])
                if(0 <= cur_position[0] < n and 0 <= cur_position[1] < m):
                    self.count_negatives(grid, directions, n, m , cur_position, count)
                else:
                    direction = directions[1]
                    cur_position = (cur_position[0]+direction[0], cur_position[1] + direction[1])
                    self.count_negatives(grid, directions, n, m , cur_position, count)
            elif(grid[cur_position[0]][cur_position[1]] >= 0):
                direction = directions[0]
                cur_position = (cur_position[0]+direction[0], cur_position[1] + direction[1])
                self.count_negatives(grid, directions, n, m, cur_position, count)
            
            