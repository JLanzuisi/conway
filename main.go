package main

func main() {
	cells := CellSet{
		Cell{1, 2}: true,
		Cell{0, 2}: true,
		Cell{2, 2}: true,
	}

	grid := Grid{cells, [2]int{10, 10}}

	// nextgen := NextGen(grid)

	// fmt.Printf("Before: %+v\n", grid.cells)
	// fmt.Printf("After: %+v\n", nextgen.cells)

	PlayPrintf(grid)
}
