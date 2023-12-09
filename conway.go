package main

import "maps"

type Cell [2]int

type CellSet map[Cell]bool

type Grid struct {
	cells CellSet
	size  [2]int
}

func Neighbors(grid Grid, cell Cell) (total int) {
	total = 0
	deltas := []Cell{
		{-1, -1},
		{-1, 0},
		{-1, 1},
		{0, 1},
		{1, 1},
		{1, 0},
		{1, -1},
		{0, -1},
	}

	for _, v := range deltas {
		row := cell[0] + v[0]
		col := cell[1] + v[1]

		if row == -1 {
			row = grid.size[0] - 1
		}
		if row == grid.size[0] {
			row = 0
		}
		if col == -1 {
			col = grid.size[1] - 1
		}
		if col == grid.size[1] {
			col = 0
		}

		n := Cell{row, col}
		exists := grid.cells[n]

		if exists {
			total++
		}
	}

	return total
}

func NextGen(grid Grid) (nextgen Grid) {
	nextgen = Grid{make(CellSet), grid.size}

	maps.Copy(nextgen.cells, grid.cells)

	for row := 0; row < grid.size[0]; row++ {
		for col := 0; col < grid.size[1]; col++ {
			cell := Cell{row, col}
			count := Neighbors(grid, cell)

			exists := grid.cells[cell]

			if exists {
				if count != 2 && count != 3 {
					delete(nextgen.cells, cell)
				}
			} else {
				if count == 3 {
					nextgen.cells[cell] = true
				}
			}
		}
	}

	return nextgen
}
