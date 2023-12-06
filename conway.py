def neighbors(cells: set, pos: tuple):
    total = 0
    for i in (-1, 1):
        if (pos[0]+i,pos[1]) in cells:
            total += 1
        if (pos[0],pos[1]+i) in cells:
            total += 1
        if (pos[0]+i,pos[1]+i) in cells:
            total += 1
        if (pos[0]-i,pos[1]+i) in cells:
            total += 1
        if total > 3:
            break
    return total

def next_gen(size: tuple, cells: set):
    next_gen = cells.copy()
    rows = size[0]
    cols = size[1]

    for row in range(rows):
        for col in range(cols):
            pos = (row, col)
            cell_neighbors = neighbors(cells, pos)
            if pos in cells:
                if cell_neighbors != 2 and cell_neighbors != 3:
                    next_gen.discard(pos)
            elif cell_neighbors == 3:
                next_gen.add(pos)
                
    return next_gen
