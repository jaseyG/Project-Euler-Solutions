import calculations

count = 1
x = 3

while count < 10001:
    if calculations.primeChecker(x):
        count += 1
        print(x, "is prime", count)
        x += 2
    else:
        x += 2

print(x - 2)