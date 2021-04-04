import shutil
import numpy as np

def create_random_grid():
    """
        Creates and returns a randomly initialized grid 
        of the same shape as the terminal window.
    """
    term = shutil.get_terminal_size()
    grid = np.random.choice([0,1],(term.lines,term.columns),p=[0.75,0.25])
    return grid

def get_grid_slice(x,y,grid):
    """
        Returns a 3x3 grid slice for the given cell.

        Inputs: x (int), y (int), grid ([][])
        Returns: sliced_grid(3x3)
    """
    # print(f'x={x} and y={y}')

    temp_grid = np.array(grid)
    sliced_grid = temp_grid[x-1:x+2,y-1:y+2]
    return sliced_grid.tolist()
    

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


def display_grid(grid):
    """
        Prints the grid in the form of a string.
        
        Inputs: grid matrix ([][])
        Returns: None
    """
    print(''.join(str(item) for innerlist in grid for item in innerlist))
    # for line in grid:
    #     line = np.array_str(line)
        # print(''.join(line))


######## TEST CODE ########
grid = create_random_grid()
# grid = [
#     [0,1,1],
#     [1,0,0],
#     [0,1,0]
# ]
display_grid(grid)
# print(get_grid_slice(1,1,grid))
###########################