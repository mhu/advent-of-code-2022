package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	input, err := os.ReadFile("../../input.txt")

	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(input), "\n")
	packets := make([]int, 1)
	index := 0

	for _, line := range lines {
		if line == "" {
			packets = append(packets, 0)
			index += 1
			continue
		}

		calories, _ := strconv.Atoi(line)
		packets[index] += calories
	}

	sort.Ints(packets)

	fmt.Println(packets[len(packets)-1])
	fmt.Println(packets[len(packets)-1] + packets[len(packets)-2] + packets[len(packets)-3])
}
