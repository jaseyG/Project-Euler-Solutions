# Project Euler 21

# NOTE: This is not efficient. It will take a few minutes
# A good starting point is to keep divisors for other numbers, instead of recalculating every single time

def find_divisors(n):
    divisors = []
    for i in  range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            if n / i not in divisors or i not in divisors:
                divisors.append(int(i))
                divisors.append(int(n / i))
    divisors.remove(n)
    return sorted(divisors)

amicable_numbers = []

for a in range(1, 10_001):
    for b in range(1, 10_001):
        if a != b:
            if sum(find_divisors(a)) == b and sum(find_divisors(b)) == a and a not in amicable_numbers and b not in amicable_numbers:
                amicable_numbers.append(a)
                amicable_numbers.append(b)

print(sum(amicable_numbers))