with open("input.txt", "r") as reader:
    datastream = reader.readline().strip()


def find_marker(num_distinct_characters: int) -> int:
    for index in range(num_distinct_characters - 1, len(datastream)):
        if len(set(datastream[index - num_distinct_characters:index])) == num_distinct_characters:
            return index


print(f"Answer 1: {find_marker(4)}")
print(f"Answer 2: {find_marker(14)}")
