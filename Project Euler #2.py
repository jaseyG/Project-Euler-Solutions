x = 1
y = 2
sum = 0

while x < 4000000 or y < 4000000:
    #Storing even values of x
    if x % 2 == 0:
        sum += x
        x += y
    else:
        x += y
        
    #Storing even values of y
    if y % 2 == 0:
        sum += y
        y += x
    else:
        y += x
        
print(sum)