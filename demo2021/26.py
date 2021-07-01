with open("26.txt") as file:
    empty_space, users_number = map(int, file.readline().split())
    files_sizes = []
    for line in file.readlines():
        files_sizes.append(int(line))

files_sizes.sort()
index = 0

while index < len(files_sizes):
    file_size = files_sizes[index]
    if empty_space >= file_size:
        empty_space -= file_size
    else:
        break
    index += 1

print(index)

previous_file_size = files_sizes[index]
max_file_size = previous_file_size
while index < len(files_sizes):
    file_size = files_sizes[index]
    if empty_space + previous_file_size >= file_size:
        max_file_size = file_size
    index += 1
print(max_file_size)
