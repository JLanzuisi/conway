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
            print(
                'This is your empty grid ('
                + str(size[0])
                + 'x'
                + str(size[1])
                + ')'
            )
            draw_grid(size, grid)
            print('Now you can mark some cells, one at a time,')
            print('by writing the coordinates into the prompt like so:')
            print('PROMPT> 0 1')
            print('or')
            print('PROMPT> 3 1')
        else:
            print('You can keep marking cells!')
            print('Send an empty prompt when done')
            print('Send u to undo')
            draw_grid(size, grid)
            
        mark = input('\nPROMPT> ')

        if not mark:
            break

        if mark == 'u':
            grid.discard(coords)
            continue
        
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
    print('Generation: ' + str(gen) + '.')
    print('Population: ' + str(len(grid)) + '.')
    
    time.sleep(0.5)
