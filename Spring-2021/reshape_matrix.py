from typing import List
class Solution:
    def __init__(self):
        self.r_ptr, self.c_ptr = 0, 0
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        if (m*n) != (r*c):
            return mat

        def mapper(i, j):
            if self.c_ptr < c:
                self.c_ptr +=1
                return (self.r_ptr, self.c_ptr-1)
            
            self.r_ptr += 1
            self.c_ptr = 1
            return (self.r_ptr, self.c_ptr-1)
        
        reshaped = [[0 for _ in range(c)] for _ in range(r)]
        
        for i in range(m):
            for j in range(n):
                new_index = mapper(i, j)
                reshaped[new_index[0]][new_index[1]] = mat[i][j]        
        
        return reshaped