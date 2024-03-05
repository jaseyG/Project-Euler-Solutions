# Project Euler 29

values = []
for a in range(2, 101):
    for b in range(2, 101):
        if a ** b not in values:
            values.append(a ** b)

print(len(values))