min_difference = -1
sum = 0

with open("27-B.txt") as file:
    file.readline()
    for line in file.readlines():
        a, b = map(int, line.split())
        sum += max(a, b)
        difference = abs(a - b)
        if min_difference < 0 or difference < min_difference and difference % 3 != 0:
            min_difference = difference

if sum % 3 == 0:
    sum -= min_difference
print(sum)
