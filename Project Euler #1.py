x = 0
y = 0
z = 1
sum3 = 0
sum5 = 0
sum35 = 0

while x < 1000:
    if x % 3 == 0:
        sum3 += x
        x += 1
    else:
        x += 1
        
print(sum3)

while y < 1000:
    if y % 5 == 0:
        sum5 += y
        y += 1
    else:
        y += 1

print(sum5)
totalSum = (sum3 + sum5)
print(totalSum)

while z < 1000:
    if z % 15 == 0:
        sum35 += z
        z += 1
    else:
        z += 1
        
print(sum35)
print("Answer is:", totalSum - sum35)