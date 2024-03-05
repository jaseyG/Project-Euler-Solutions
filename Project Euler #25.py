# Project Euler 25

from euler import calculations

n = False
count = 4000
while n == False:
    if len(str(calculations.fibonacci(count))) < 1000:
           count += 1
    else:
        n = True
print(count)