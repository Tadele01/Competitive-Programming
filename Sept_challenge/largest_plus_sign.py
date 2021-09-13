from typing import List
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        matrix, self.cache = [[1 for _ in range(n)] for _ in range(n)], {}
        for r, c in mines:
            matrix[r][c] = 0
            
        res = 0
        cache = [[[0,0,0,0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    cache[i][j][0]=(cache[i][j-1][0]+1) if j-1>=0 else 1
                    cache[i][j][1]=(cache[i-1][j][1]+1) if i-1>=0 else 1
                    res = max(res, 1)
                    
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if matrix[i][j] == 1:
                    cache[i][j][2]=(cache[i][j+1][2]+1) if j+1<n else 1
                    cache[i][j][3]=(cache[i+1][j][3]+1) if i+1<n else 1
                    res = max(res, 1)
                    
                res = max(res, min(cache[i][j]))
                
        return res   
                                    
                                