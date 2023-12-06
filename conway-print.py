import conway
import time
import os

def draw_grid(size:tuple, grid: set):
    for row in range (size[0]):
        current_line = ''
        for col in range(size[1]):
            pos = (row, col)
            if pos in grid:
                current_line += '⬜ '
            else:
                current_line += '⬛ '
        print(current_line)

def grid_setup(size, grid):
    while True:
        os.system('clear')
        if not grid:
            print('This is your empty grid:')
            draw_grid(size, grid)
            print('Now you can mark some cells, one at a time, like so \'0 1\'')
            print('''When you're done press enter''')
        else:
            print('You can keep marking cells! (Press Enter when done)')
            draw_grid(size, grid)
        mark = input()

        if not mark:
            break
    
        coords = tuple(map(int, mark.split(' ')))
        grid.add(coords)
        draw_grid(size, grid)

    return grid

N = 10
M = 10
size = (N, M)
grid = set()
sep = ''

grid = grid_setup(size, grid)

for i in range (30):
    sep += '─'

gen = 0
while grid:
    os.system('clear')
    gen += 1
    
    print('''Now we'll simulate with your input:''')
    
    grid = conway.next_gen(size, grid)
    draw_grid(size, grid)
    
    print(sep)
    print('INFO:')
    print('Current generation: ' + str(gen) + '.')
    print('Live cells: ' + str(len(grid)) + '.')
    
    time.sleep(2)

# TODO
# Unmark a cell.
# Pause, play?
