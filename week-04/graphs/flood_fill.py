class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        if image[sr][sc] == newColor:
            return image
        
        neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.dfs(image, (sr, sc), newColor, image[sr][sc], neighbours)
        return image
    
    def dfs(self, image, point, new_color, starting_color, neighbours):
        image[point[0]][point[1]] = new_color
        
        for neighbour in neighbours:
            new_r = point[0] + neighbour[0]
            new_c = point[1] + neighbour[1] 
            if 0 <= new_r < len(image) and \
                0 <= new_c < len(image[0]) and \
                 image[new_r][new_c] == starting_color:
                        self.dfs(image, (new_r, new_c), new_color, starting_color, neighbours)