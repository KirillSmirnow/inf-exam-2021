with open("24.txt") as file:
    content = file.read().replace('\n', '')

max_sequence_length = 0
sequence_length = 0
previous_char = ''

for char in content:
    if char != previous_char:
        sequence_length += 1
    else:
        if sequence_length > max_sequence_length:
            max_sequence_length = sequence_length
        sequence_length = 1
    previous_char = char

print(max_sequence_length)
