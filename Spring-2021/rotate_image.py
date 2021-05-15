from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        tmp = []
        for i in range(len(matrix)):
            arr = []
            for j in range(len(matrix[i])):
                arr.append(matrix[i][j])
                
            tmp.append(arr)
        
        col = 0
        
        for i in range(len(matrix)):
            row = len(matrix) -1 
            for j in range(len(matrix[i])):
                matrix[i][j] = tmp[row][col]
                row -= 1
            col += 1
                        
        return matrix
                
        