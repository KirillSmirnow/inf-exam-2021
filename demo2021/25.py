for number in range(174457, 174505 + 1):
    divisors = []
    for i in range(2, number):
        if number % i == 0:
            divisors.append(i)
    if len(divisors) == 2:
        print("%6i %6i" % (divisors[0], divisors[1]))
