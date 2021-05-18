class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        new_matrix, stones = [], set()
        
        for i in range(len(box[0])):
            col = []
            for j in range(len(box)):
                col.append(box[j][i])
                if box[j][i] == '#':
                    stones.add((i, j))
            new_matrix.append(col)
            
        move = (1, 0)
        num_row, num_col = len(new_matrix), len(new_matrix[0])
        stones = list(stones)
        stones.sort(reverse=True)
        while stones:
            row, col = stones[0][0], stones[0][1]
            cp_r, cp_c = row, col
            while True:
                new_r, new_c = row+move[0], col+move[1]
                if new_r < num_row and new_c < num_col and new_matrix[new_r][new_c] == '.':
                    new_matrix[row][col] = '.'
                    new_matrix[new_r][new_c] = '#'
                    row, col = new_r, new_c
                else:
                    stones.remove((cp_r, cp_c))
                    break
        for i in range(len(new_matrix)):
            new_matrix[i] = list(reversed(new_matrix[i]))
        
                    
        return new_matrix
        
        