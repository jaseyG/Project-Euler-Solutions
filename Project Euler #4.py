import calculations

x = 999
y = 999
products = []
loop = False

while loop == False:
    if calculations.palindromeChecker(x*y):
        products.append(x*y)
        x -= 1
    elif x > 0:
        x -= 1
    elif y == 1:
        loop = True
    else:
        y -= 1
        x = y

print(max(products))