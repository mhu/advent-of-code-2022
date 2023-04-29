contents = open("input.txt", "r").read().splitlines()

head_pos = (0, 0)
tail_pos = (0, 0)
tail_pos_visited = set()

for rule in contents:
    direction, amount = rule.split(" ")

    for step in range(int(amount)):
        if direction == "R":
            head_pos = (head_pos[0] + 1, head_pos[1])
        elif direction == "L":
            head_pos = (head_pos[0] - 1, head_pos[1])
        elif direction == "U":
            head_pos = (head_pos[0], head_pos[1] + 1)
        elif direction == "D":
            head_pos = (head_pos[0], head_pos[1] - 1)

        if head_pos[0] == tail_pos[0] + 2:
            tail_pos = (tail_pos[0] + 1, head_pos[1])
        elif head_pos[0] == tail_pos[0] - 2:
            tail_pos = (tail_pos[0] - 1, head_pos[1])
        elif head_pos[1] == tail_pos[1] + 2:
            tail_pos = (head_pos[0], tail_pos[1] + 1)
        elif head_pos[1] == tail_pos[1] - 2:
            tail_pos = (head_pos[0], tail_pos[1] - 1)

        print(tail_pos)
        tail_pos_visited.add(tail_pos)

print(len(tail_pos_visited))
