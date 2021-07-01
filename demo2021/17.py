def is_number_of_interest(number):
    return number % 3 == 0 and number % 7 != 0 and number % 17 != 0 and number % 19 != 0 and number % 27 != 0


numbers_count = 0
max_number = 0
for number in range(1016, 7937 + 1):
    if is_number_of_interest(number):
        numbers_count += 1
        if number > max_number:
            max_number = number
print(numbers_count)
print(max_number)
