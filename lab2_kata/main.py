import random
import time

def init_grid(grid, rows, cols, seed):
    random.seed(seed)
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.choice([0,1]))
        grid.append(row)
        
def print_grid(grid, rows, cols):
    for row in range(rows):
        for col in range(cols):
            print(" O" if grid[row][col] else " .", end="")
        print()
    print("---------------------------------------------------")


def count_neighbours(grid, row, col, rows, cols):
    neighbours = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            r = row + i
            c = col + j
            if 0 <= r < rows and 0 <= c < cols:
                neighbours += grid[r][c]
    return neighbours

def next_generation(grid, rows, cols):
    new_grid = [[0]*cols for i in range(rows)]
    for row in range(rows):
        for col in range(cols):
            n = count_neighbours(grid, row, col, rows, cols)
            if grid[row][col] and n in (2, 3):
                new_grid[row][col] = 1
            elif not grid[row][col] and n == 3:
                new_grid[row][col] = 1
    return new_grid
                
    
if __name__=="__main__":
    rows, cols = 20, 20
    grid = []
    init_grid(grid, rows, cols, 3)
    
    
    while True:
        print_grid(grid, rows, cols)
        grid = next_generation(grid, rows, cols)
        time.sleep(0.2)
        