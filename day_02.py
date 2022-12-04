rounds = [n.strip() for n in open("input.txt", "r")]

# puzzle 1

total_points = 0

for current_round in rounds:
    opponent, me = current_round.split(" ")

    match me:
        case "X":
            total_points = total_points + 1
            total_points = total_points + 6 if opponent == "C" else total_points
            total_points = total_points + 3 if opponent == "A" else total_points
        case "Y":
            total_points = total_points + 2
            total_points = total_points + 6 if opponent == "A" else total_points
            total_points = total_points + 3 if opponent == "B" else total_points
        case "Z":
            total_points = total_points + 3
            total_points = total_points + 6 if opponent == "B" else total_points
            total_points = total_points + 3 if opponent == "C" else total_points

print(f"Answer 1: {total_points}")

# puzzle 2

total_points = 0

matchup_dict = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}

for current_round in rounds:
    total_points = total_points + matchup_dict[current_round]

print(f"Answer 2: {total_points}")
