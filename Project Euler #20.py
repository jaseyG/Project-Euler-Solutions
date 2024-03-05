# Project Euler 20

def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

total = 0
numba = str(factorial(100))
for i in numba:
    total += int(i)

print(total)

