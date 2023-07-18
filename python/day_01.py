elves = []

with open('input.txt', 'r') as inputs:
    current_calories = 0

    for n in inputs:
        n = n.strip()

        if n == "":
            elves.append(current_calories)
            current_calories = 0
            continue

        current_calories += int(n)

    elves.append(current_calories) # don't forget to push the last value

print(f"Answer 1: {max(elves)}")
print(f"Answer 2: {sum(sorted(elves)[-3:])}")
