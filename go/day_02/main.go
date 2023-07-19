package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	input, err := os.ReadFile("../../input.txt")

	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(input), "\n")
	total_points_part_1 := 0
	total_points_part_2 := 0

	for _, line := range lines {
		if line == "" {
			continue
		}

		shapes := strings.Split(line, " ")
		opponent, me := shapes[0], shapes[1]

		// opp - A: rock, B: paper, C: scissors
		// me  - X: rock, Y: paper, Z: scissors

		if me == "X" {
			total_points_part_1 += 1
		} else if me == "Y" {
			total_points_part_1 += 2
		} else if me == "Z" {
			total_points_part_1 += 3
		}

		if me == "X" && opponent == "C" {
			total_points_part_1 += 6
		} else if me == "Y" && opponent == "A" {
			total_points_part_1 += 6
		} else if me == "Z" && opponent == "B" {
			total_points_part_1 += 6
		}

		if me == "X" && opponent == "A" {
			total_points_part_1 += 3
		} else if me == "Y" && opponent == "B" {
			total_points_part_1 += 3
		} else if me == "Z" && opponent == "C" {
			total_points_part_1 += 3
		}

		if me == "X" && opponent == "B" {
			total_points_part_1 += 0
		} else if me == "Y" && opponent == "C" {
			total_points_part_1 += 0
		} else if me == "Z" && opponent == "A" {
			total_points_part_1 += 0
		}

		switch line {
		case "A X":
			total_points_part_2 += 3
		case "A Y":
			total_points_part_2 += 4
		case "A Z":
			total_points_part_2 += 8
		case "B X":
			total_points_part_2 += 1
		case "B Y":
			total_points_part_2 += 5
		case "B Z":
			total_points_part_2 += 9
		case "C X":
			total_points_part_2 += 2
		case "C Y":
			total_points_part_2 += 6
		case "C Z":
			total_points_part_2 += 7
		}
	}

	fmt.Println(total_points_part_1)
	fmt.Println(total_points_part_2)
}
