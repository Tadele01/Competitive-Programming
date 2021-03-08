def is_valid(new_r, new_c, num_row, num_col):
    if 0<= new_r < num_row and 0<= new_c < num_col:
        return True
    return False
def surfaceArea(A):
    surface_area, directions = 0, [(0, 1), (0, -1), (1, 0), (-1, 0)]
    num_row, num_col = len(A), len(A[0])
    height, width = 1, 1
    for row in range(num_row):
        for col in range(num_col):
            surface_area += 2 #for top and bottom area
            for direction in directions:
                new_r, new_c = row+direction[0], col+direction[1]
                if is_valid(new_r, new_c, num_row, num_col) and A[row][col] > A[new_r][new_c]:
                    seen_surface = A[row][col] - A[new_r][new_c]
                    surface_area += seen_surface
                elif not is_valid(new_r, new_c, num_row, num_col):
                    surface_area += A[row][col]
    return surface_area
    