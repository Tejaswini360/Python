print("Name:Tejaswini M",
       "AUID:1AY24AI111",
       "Section:O")
import time
import os

# Define grid size
WIDTH = 10
HEIGHT = 10

# Create an initial grid (0 = dead, 1 = alive)
grid = [[0]*WIDTH for _ in range(HEIGHT)]

# Add a simple pattern (a "blinker")
grid[4][4] = 1
grid[4][5] = 1
grid[4][6] = 1

def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        for cell in row:
            print('■' if cell else ' ', end='')
        print()
    print()

def get_neighbors(x, y, grid):
    neighbors = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            ni, nj = y + i, x + j
            if 0 <= ni < HEIGHT and 0 <= nj < WIDTH:
                neighbors += grid[ni][nj]
    return neighbors

def next_generation(grid):
    new_grid = [[0]*WIDTH for _ in range(HEIGHT)]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            neighbors = get_neighbors(x, y, grid)
            if grid[y][x] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_grid[y][x] = 1
            else:
                if neighbors == 3:
                    new_grid[y][x] = 1
    return new_grid

# Run the simulation
try:
  while True:
        print_grid(grid)
        grid = next_generation(grid)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nGame stopped.")

