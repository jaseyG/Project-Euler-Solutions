# Project Euler 12
from math import sqrt

def count_divisors(n):
    count = 0
    sqrt_n = int(sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 2  # Count both divisors i and n/i
    if sqrt_n * sqrt_n == n:  # If perfect square, subtract one divisor
        count -= 1
    return count

divisors = 0
term = 1
while divisors <= 500:
    num = term * (term + 1) // 2
    divisors = count_divisors(num)
    term += 1

print(num)