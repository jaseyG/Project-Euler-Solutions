import math

for a in range(0, 499):
    for b in range(0, 499):
        c = math.sqrt(a**2 + b**2)
        if a + b + c == 1000:
            print(a*b*c)
            