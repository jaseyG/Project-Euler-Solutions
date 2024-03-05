x = 1
y = 1

while y <= 20:
        if x % y == 0:
            y += 1
        else:
            x += 1
            y = 1

print(x)