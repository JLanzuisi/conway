package main

import "fmt"
import "maps"

type Pair struct {
	x int
	y int
}

type Cell Pair

type CellSet map[Cell]bool

type Grid struct {
	cells CellSet
	n     int
	m     int
}

func neighbors(grid Grid, cell Cell) (total int) {
	total = 0
	deltas := []Pair{
		Pair{-1, -1},
		Pair{-1, 0},
		Pair{-1, 1},
		Pair{0, 1},
		Pair{1, 1},
		Pair{1, 0},
		Pair{1, -1},
		Pair{0, -1},
	}

	for _, v := range deltas {
		row := cell.x + v.x
		col := cell.y + v.y

		if row == -1 {
			row = grid.n - 1
		}
		if row == grid.n {
			row = 0
		}
		if col == -1 {
			col = grid.m - 1
		}
		if col == grid.m {
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
	nextgen = Grid{make(CellSet), grid.n, grid.m}

	maps.Copy(nextgen.cells, grid.cells)

	for row := 0; row < grid.n; row++ {
		for col := 0; col < grid.m; col++ {
			cell := Cell{x: row, y: col}
			count := neighbors(grid, cell)

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

func main() {
	cells := CellSet{
		Cell{1, 2}: true,
		Cell{0, 2}: true,
		Cell{2, 2}: true,
	}

	grid := Grid{cells, 10, 10}

	nextgen := NextGen(grid)

	fmt.Printf("Before: %+v\n", grid.cells)
	fmt.Printf("After: %+v\n", nextgen.cells)
}
