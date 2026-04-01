import random
import time

def init_grid(seed, rows,cols):
    random.seed(seed)
    grid = []
    for i in range(rows):   
        row = []
        for j in range(cols):
            row.append(random.randint(0,1))
        grid.append(row)
    return grid
    
def print_grid(grid, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print('O' if grid[i][j] else '.', end=" ")
            #print(grid[i][j], end=" ")
        print()

def count_neighbors(grid, row, col, rows, cols):
    neighbors = 0
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr == 0 and dc == 0:
                continue  
            r = row + dr
            c = col + dc
            if 0 <= r < rows and 0 <= c < cols:  
                neighbors += grid[r][c]
    return neighbors

def next_generation(grid, rows, cols):
    new_grid = [[0]*cols for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            n = count_neighbors(grid, row, col, rows, cols)
            if grid[row][col] and n in (2, 3):
                new_grid[row][col] = 1
            elif not grid[row][col] and n == 3:
                new_grid[row][col] = 1
            else:
                new_grid[row][col] = 0
    return new_grid
                    
def test():
    rows = 20
    cols = 20
    grid = init_grid(rows, cols)
    print_grid(grid, rows, cols)
    
    print(count_neighbors(grid, 1,2, rows, cols))
    
if __name__ == "__main__":
    rows, cols = 20, 20
    grid = init_grid(13, rows, cols)
    while True:
        print("\033[H\033[J", end="") 
        print_grid(grid, rows, cols)
        grid = next_generation(grid, rows, cols)
        time.sleep(1)