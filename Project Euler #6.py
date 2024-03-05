x = 0
square = 0
sum = 0

while x <= 100:
    square = square + x**2
    sum += x
    x += 1
    
sum = sum**2
print(abs(square-sum))

