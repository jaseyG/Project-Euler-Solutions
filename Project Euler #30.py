# Project Euler 30
total = 0
values = []
for i in range(1, 200_000):
    numba = str(i)
    for letter in numba:
        total += int(letter)**5
    if total == i:
        values.append(i)
    total = 0
    
values.remove(1)
print(sum(values))