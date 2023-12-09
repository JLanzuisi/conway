package main

import "fmt"

func DrawGrid(grid Grid) {
	for row := 0; row < grid.size[0]; row++ {
		line := ""
		for col := 0; col < grid.size[1]; col++ {
			exists := grid.cells[Cell{row, col}]

			if exists {
				line += "⬜ "
			} else {
				line += "⬛ "
			}
		}
		fmt.Println(line)
	}
}
