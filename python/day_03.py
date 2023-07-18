import string

rucksacks = [l.strip() for l in open("input.txt", "r")]

def get_priorities(items) -> int:
    priorities = 0
    all_ascii = string.ascii_lowercase + string.ascii_uppercase

    for item in items:
        priorities = priorities + all_ascii.index(item) + 1

    return priorities

# puzzle 1

common_items = []

for rucksack in rucksacks:
    middle = int(len(rucksack) / 2)
    compartments = rucksack[:middle], rucksack[middle:]
    common_items.append("".join(set(compartments[0]).intersection(set(compartments[1]))))

print(f"Answer 1: {get_priorities(common_items)}")

# puzzle 2

common_items = []
groups = list(map(lambda *x: x, *([iter(rucksacks)] * 3)))

for group in groups:
    common_items.append(
        "".join(
            set(group[0])
            .intersection(set(group[1]))
            .intersection(set(group[2]))
        )
    )

print(f"Answer 2: {get_priorities(common_items)}")
