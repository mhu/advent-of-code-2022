elves = [l.strip() for l in open("input.txt", "r")]

num_intersections = 0

for elf in elves:
    sections = elf.split(",")

    first_elf_rooms = [int(n) for n in sections[0].split("-")]
    second_elf_rooms = [int(n) for n in sections[1].split("-")]

    if first_elf_rooms[0] <= second_elf_rooms[0] and first_elf_rooms[1] >= second_elf_rooms[1]:
        num_intersections = num_intersections + 1
    elif second_elf_rooms[0] <= first_elf_rooms[0] and second_elf_rooms[1] >= first_elf_rooms[1]:
        num_intersections = num_intersections + 1

print(f"Answer 1: {num_intersections}")

num_intersections = 0

for elf in elves:
    sections = sorted(elf.split(","))

    first_elf_rooms = [int(n) for n in sections[0].split("-")]
    second_elf_rooms = [int(n) for n in sections[1].split("-")]

    if first_elf_rooms[0] >= second_elf_rooms[0] and first_elf_rooms[0] <= second_elf_rooms[1]:
        num_intersections = num_intersections + 1
    elif first_elf_rooms[1] >= second_elf_rooms[0] and first_elf_rooms[1] <= second_elf_rooms[1]:
        num_intersections = num_intersections + 1
    elif first_elf_rooms[0] <= second_elf_rooms[0] and first_elf_rooms[1] >= second_elf_rooms[1]:
        num_intersections = num_intersections + 1
    elif second_elf_rooms[0] <= first_elf_rooms[0] and second_elf_rooms[1] >= first_elf_rooms[1]:
        num_intersections = num_intersections + 1

print(f"Answer 2: {num_intersections}")
