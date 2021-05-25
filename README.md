# Game of Life

The [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), also known simply as **Life**, is a cellular automaton. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. 

<img src="https://user-images.githubusercontent.com/70139937/119540949-a62daa80-bdab-11eb-826c-5e1a18bf9e3c.gif" width="300" height="300" align="center"/>

## Rules

The Game of Life consists of a two dimensional grid (usually squares) consisting of **cells**, which are in either of two states: alive, or dead. Each cell interacts with its adjacent neighbours; at each step in time, the following transitions can occur:<br/><br/>
1  Any live cell with two or three live neighbours survives.<br/>
2. Any dead cell with three live neighbours becomes a live cell.<br/>
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.


## Implementation

This has been implemented by plotting the grid as a heatmap using the matplotlib module. The plot also displays the iteration number as well as the number of active (living) cells on the grid at each iteration.


## Cloning the repository

```
git clone https://github.com/prateek-joshi/Game-of-Life.git
```


## Requirements

```
matplotlib==3.3.4
numpy==1.20.1
```


## Running the application

```
cd Game-of-Life\Game-of-Life
python main.py
```
