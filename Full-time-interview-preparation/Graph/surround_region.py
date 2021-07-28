from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or j == 0 or i == rows-1 or j == cols - 1) and board[i][j] == 'O':     
                    board[i][j] = '-'
                    self.dfs(board, i, j)
                    
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    
    def dfs(self, board, i, j):
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            r, c = i + x, j + y
            if 0<= r < len(board) and 0<= c < len(board[0]) and board[r][c] == 'O': 
                board[r][c] = '-'
                self.dfs(board, r, c)


    
    
        
                    
        
        
        
                
        
                
        