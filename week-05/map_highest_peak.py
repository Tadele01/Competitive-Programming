from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (-1,0),(1, 0)]
        queue, num_row, num_col = deque(), len(isWater), len(isWater[0])
        visited = set()
        for row in range(num_row):
            for col in range(num_col):
                if isWater[row][col] == 1:
                    isWater[row][col] = 0
                    queue.append((row, col))
                    visited.add((row, col))
        while queue:
            cur_pos = queue.popleft()
            for direction in directions:
                new_r, new_c = direction[0]+cur_pos[0], direction[1]+cur_pos[1]
                if self.is_valid(new_r, new_c, isWater, visited):
                    isWater[new_r][new_c] = isWater[cur_pos[0]][cur_pos[1]] + 1
                    queue.append((new_r, new_c))
        return isWater
    def is_valid(self, new_r, new_c, isWater, visited):
        num_row, num_col = len(isWater), len(isWater[0])
        if (new_r, new_c) not in visited:
            visited.add((new_r, new_c))
            if 0<= new_r < num_row and 0<= new_c < num_col:
                return True
            return False
        return False
        