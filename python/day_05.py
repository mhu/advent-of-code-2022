def prepare_data() -> (dict, list):
    crates = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
    }

    rules = []

    for line in open("input.txt", "r"):
        if line.strip() == "":
            continue

        if line.startswith("move"):
            rules.append(format_rule(line.strip()))
            continue

        append_to_crates(crates, line)

    for crate in crates.values():
        crate.pop(0)

    return crates, rules


def format_rule(rule: str) -> tuple[int]:
    split = rule.split(" ")
    return int(split[1]), int(split[3]), int(split[5])


def append_to_crates(crates: dict, line: str) -> None:
    positions_to_check = [1, 5, 9, 13, 17, 21, 25, 29, 33]

    for position in positions_to_check:
        if line[position] != " ":
            crates[positions_to_check.index(position) + 1].insert(0, line[position])


# puzzle 1

crates, rules = prepare_data()

for amount, crates_from, crates_to in rules:
    for _ in range(amount):
        crates[crates_to].append(crates[crates_from].pop())

answer = "".join([c[-1] for c in crates.values()])
print(f"Answer 1: {answer}")

# puzzle 2

crates, rules = prepare_data()

for amount, crates_from, crates_to in rules:
    moved_crates = crates[crates_from][-amount:]
    crates[crates_from] = crates[crates_from][:-amount]
    crates[crates_to] = crates[crates_to] + moved_crates

answer = "".join([c[-1] for c in crates.values()])
print(f"Answer 2: {answer}")
