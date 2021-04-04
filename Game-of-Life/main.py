import shutil
import numpy as np

def create_random_grid():
    """
        Creates and returns a randomly initialized grid 
        of the same shape as the terminal window.
    """
    term = shutil.get_terminal_size()
    grid = np.random.choice([0,1],(term.lines,term.columns),p=[0.9,0.1])
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
    

def count_living_cells(grid):
    """
        Returns the number of live cells surrounding the current center.
        
        Inputs: grid (3x3)\n
        Returns: count_lives (int)
    """
    return np.sum(grid)


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
print("Number of active elements: "+str(count_living_cells(grid)))
# print(get_grid_slice(1,1,grid))
###########################