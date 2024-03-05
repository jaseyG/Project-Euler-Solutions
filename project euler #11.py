#Project Euler 11
product = []

f = open('number.txt', 'r')
text = f.readlines()

grid = []
grid2 = []

for string in text:
    holder = string.replace('\n', '')
    holder2 = holder.replace(' ', ',')
    grid.append(holder2.split(','))

temp = []
for row in grid:
    for item in row:
        temp.append(int(item))
    grid2.append(temp)
    temp = []
    
for row in grid2: #horizontalally adjacent
    for i, value in enumerate(row):
        if i <= 16:
            product.append(row[i] * row[i + 1] * row[i + 2] * row[i + 3])
         
for i in range(17): #vertically adjacent
    for j in range(20):
        product.append(grid2[i][j] * grid2[i + 1][j] * grid2[i + 2][j] * grid2[i + 3][j])
        
for r_i in range(17): #diagonally adjacent
    for c_i in range(17):
        product.append(grid2[r_i][c_i] * grid2[r_i + 1][c_i + 1] * grid2[r_i + 2][c_i + 2] * grid2[r_i + 3][c_i + 3])
        
for r_i in range(19, -1, -1):
    if r_i >= 3:
        for c_i in range(0, 17):
                product.append(grid2[r_i][c_i] * grid2[r_i - 1][c_i + 1] * grid2[r_i - 2][c_i + 2] * grid2[r_i - 3][c_i + 3])

print(max(product))