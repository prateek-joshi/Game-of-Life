import sys, os
import numpy as np

def game_of_life_cell(grid):
    x,y = len(grid)//2, len(grid[0])//2
    count_live = 0
    # return x,y
    
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if (i==x and j==y):
                continue
            count_live += grid[i][j]
    
    return count_live

grid = [
    [0, 1, 1],
    [1, 1, 1],
    [0, 0, 0]
]

print(game_of_life_cell(grid))