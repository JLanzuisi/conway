def neighbors(cells: set, pos: tuple, size: tuple):
    total = 0
    row = pos[0]
    col = pos[1]
    N = size[0]
    M = size[1]
    
    for i in (-1, 1):
        # Rows
        if row+i == -1:
            if (N-1, col) in cells:
                total += 1
        elif row+i == N:
            if (0, col) in cells:
                total += 1
        else:
            if (row+i, col) in cells:
                total += 1
        # Columns
        if col+i == -1:
            if (row, M-1) in cells:
                total += 1
        elif col+i == M:
            if (row, 0) in cells:
                total += 1
        else:
            if (row, col+i) in cells:
                total += 1
        # Diagonals
        # Same sing
        if row+i == -1 and col+i == -1:
            if (N-1, M-1) in cells:
                total += 1
        elif row+i == -1:
            if (N-1, col+i) in cells:
                total += 1
        elif col+i == -1:
            if (row+i, M-1) in cells:
                total += 1
        elif row+i == N and col+i == M:
            if (0, 0) in cells:
                total += 1
        elif row+i == N:
            if (0, col+i) in cells:
                total += 1
        elif col+i == M:
            if (row+i, 0) in cells:
                total += 1
        else:
            if (row+i ,col+i) in cells:
                total += 1
        # Oppositte sing
        if row-i == -1 and col+i == -1:
            if (N-1, M-1) in cells:
                total += 1
        elif row-i == -1:
            if (N-1, col+i) in cells:
                total += 1
        elif col+i == -1:
            if (row-i, M-1) in cells:
                total += 1
        elif row-i == N and col+i == M:
            if (0, 0) in cells:
                total += 1
        elif row-i == N:
            if (0, col+i) in cells:
                total += 1
        elif col+i == M:
            if (row-i, 0) in cells:
                total += 1
        else:
            if (row-i ,col+i) in cells:
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
            cell_neighbors = neighbors(cells, pos, size)
            if pos in cells:
                if cell_neighbors != 2 and cell_neighbors != 3:
                    next_gen.discard(pos)
            elif cell_neighbors == 3:
                next_gen.add(pos)
                
    return next_gen
