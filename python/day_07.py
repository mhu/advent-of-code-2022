directories = {}
current_directory = None

# possible patterns for lines:
# $ cd /
# $ cd ..
# $ cd foo
# $ ls
# dir bar
# 143562 baz

with open("input.txt", "r") as reader:
    for line in reader.readlines():
        line = line.strip()

        if line.startswith("$ cd"):
            if line == "$ cd /":
                current_directory = "/"
            elif line == "$ cd ..":
                if current_directory.count("/") == 1:
                    current_directory = "/"
                else:
                    current_directory = "/".join(current_directory.split("/")[:-1])
            else:
                new_directory = line.split(" ")[-1]
                if current_directory == "/":
                    current_directory = "/" + new_directory
                else:
                    current_directory = f"{current_directory}/{new_directory}"

            if current_directory not in directories:
                directories[current_directory] = 0

        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            pass
        else: # e.g. "143562 baz"
            filesize = int(line.split(" ")[0])
            directories[current_directory] += filesize

            if current_directory != "/":
                parent_directory = "/".join(current_directory.split("/")[:-1])
                while parent_directory.count("/") > 0:
                    directories[parent_directory] += filesize
                    parent_directory = "/".join(parent_directory.split("/")[:-1])
                directories["/"] += filesize

total_filesize_under_100k = 0

for filesize in directories.values():
    if filesize <= 100_000:
        total_filesize_under_100k += filesize

print(f"Answer 1: {total_filesize_under_100k}")

total_disk_space = 70_000_000
total_disk_space_required = 30_000_000
used_disk_space = directories["/"]
unused_disk_space = total_disk_space - used_disk_space
disk_space_to_delete = total_disk_space_required - unused_disk_space

directory_to_delete = "/"
for directory, filesize in directories.items():
    if filesize >= disk_space_to_delete:
        if filesize < directories[directory_to_delete]:
            directory_to_delete = directory

print(f"Answer 2: {directories[directory_to_delete]}")
