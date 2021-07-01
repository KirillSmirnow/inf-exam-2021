def f(n):
    n = n * 2 + bin(n).count("1") % 2
    n = n * 2 + bin(n).count("1") % 2
    return n


for n in range(1, 30):
    if f(n) > 77:
        print(n)
