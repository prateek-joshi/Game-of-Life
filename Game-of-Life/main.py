import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 100

def create_random_grid():
    """
        Creates and returns a randomly initialized grid 
        of the same shape as the terminal window.
    """
    grid = np.random.choice([0,1],(N,N),p=[0.9,0.1])
    return grid
    

def count_living_cells(grid,i,j):
    """
        Returns the number of live cells surrounding the current center.\n\n
        
        Inputs: grid (3x3), i (int), j (int)\n
        Returns: count_lives (int)
    """
    # return np.sum(grid)
    total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]))
    return total



def evolve(grid):
    """
        Returns the evolved version of the grid by following\n
        the rules of the Game of Life.
    """
    new_grid = grid.copy()
    for row in range(1,N):
        for column in range(1,N):
            # print(row,column)
            if grid[row][column] == 0:   # Cell is dead
                if count_living_cells(grid,row,column) == 3:   # Neighbouring cells are exactly three
                    # print('Neigboring cells = 3')
                    new_grid[row][column] = 1   # Cell turns alive
            
            elif grid[row][column] == 1:    # Cell is alive
                if count_living_cells(grid,row,column) < 2:    # Cell neigbours are less than two or greater than three die
                    # print('Neigboring cells = less than 2')
                    new_grid[row][column] = 0
                elif count_living_cells(grid,row,column) > 3:
                    # print('Neigboring cells = more than 3')
                    new_grid[row][column] = 0
        
    return new_grid


def update(curr):
    """
        Called multiple times by the FuncAnimation function.\n
        Plots the new grid on the axes.
    """
    if curr==300:
        a.event_source.stop()
    global i, grid
    plt.cla()
    grid = evolve(grid)
    plt.gca().imshow(grid, interpolation='nearest')
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.gca().set_title(f'Iteration No. {i+1}\nNumber of living cells: {np.sum(grid)}')
    plt.show()
    i += 1


######## TEST CODE ########
if __name__=='__main__':
    i = 0
    fig = plt.figure()
    grid = create_random_grid()
    plt.gca().imshow(grid, interpolation='nearest')
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.gca().set_title(f'Number of living cells: {np.sum(grid)}')

    a = animation.FuncAnimation(
        fig,
        update,
        interval=250
    )
    plt.show()
###########################