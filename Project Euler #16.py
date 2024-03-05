# Project Euler 16

value = 2
for i in range(1, 1000):
    value = value * 2
    
value = str(value)
sum = 0
for i in value:
    sum += int(i)

print(sum)