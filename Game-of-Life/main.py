import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_random_grid():
    """
        Creates and returns a randomly initialized grid 
        of the same shape as the terminal window.
    """
    N = 25
    grid = np.random.choice([0,1],(N,N),p=[0.9,0.1])
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
    return '\nNumber of active elements: '+str(np.sum(grid))


def evolve_cell(grid, x, y):
    """
        Returns the evolved version of the cell center.
        Modifies the gri in place.
    """
    sliced_grid = get_grid_slice(x,y,grid)
    print(sliced_grid)
    print(count_living_cells(sliced_grid))


# def show_output(grid):
#     fig, ax = plt.subplots()
#     ax.imshow(grid, interpolation='nearest')
#     ax.axes.get_xaxis().set_visible(False)
#     ax.axes.get_yaxis().set_visible(False)
#     return fig,ax

def update(curr):
    if curr==100:
        a.event_source.stop()
    grid = create_random_grid()
    plt.cla()
    plt.gca().imshow(grid, interpolation='nearest')
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.gca().set_title(count_living_cells(grid))
    plt.show()


######## TEST CODE ########
if __name__=='__main__':
    fig = plt.figure()
    a = animation.FuncAnimation(
        fig,
        update,
        interval=100
    )
    plt.show()
###########################