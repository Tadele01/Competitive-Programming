class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_path = 0
        cache = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                path_len = 1 + self.dfs(matrix, row, col, cache)
                max_path = max(max_path, path_len)
                
        return max_path
        
        
    def dfs(self, matrix, row, col, cache):
        def is_valid(pos, new_pos):
            if 0 <= new_pos[0] < len(matrix) and 0 <= new_pos[1] < len(matrix[0]) and matrix[new_pos[0]]                            [new_pos[1]] > matrix[pos[0]][pos[1]] :
                return True
            return False
            
        if (row, col) in cache:
            return cache[(row, col)]
        
        path = max(1 + self.dfs(matrix, row+1, col, cache) if is_valid((row, col), (row+1, col)) else 0, 
                   
                   1 + self.dfs(matrix, row-1, col, cache) if is_valid((row, col), (row-1, col)) else 0,
                   
                   1 + self.dfs(matrix, row, col+1, cache) if is_valid((row, col), (row, col+1))else 0, 
                   
                   1 + self.dfs(matrix, row, col-1, cache) if is_valid((row, col), (row, col-1)) else 0
             )
        cache[(row, col)] = path
        return cache[(row, col)]
        