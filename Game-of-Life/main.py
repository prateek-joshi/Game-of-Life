import sys, os
import numpy as np

def get_grid_slice(x,y,grid):
    """
        Returns a 3x3 grid slice for the given cell.

        Inputs: x (int), y (int), grid ([][])
        Returns: sliced_grid(3x3)
    """
    print(f'x={x} and y={y}')

    sliced_grid = [row[y-1:y+2] for row in grid[x-1:x+2]]
    # return grid[x-1:x+1][y-1:y+1]
    return sliced_grid
    

def game_of_life_cell(grid):
    """
        Returns the number of live cells surrounding the current center.
        
        Inputs: grid (3x3)\n
        Returns: count_lives (int)
    """
    x,y = len(grid)//2, len(grid[0])//2
    count_live = 0
    # return x,y
    
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if (i==x and j==y):
                continue
            count_live += grid[i][j]
    
    return count_live

######## TEST CODE ########
grid = [
    [0, 1, 1, 1],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 1]
]
# print(game_of_life_cell(grid))
sliced = get_grid_slice(1,1,grid)
print(sliced)
###########################