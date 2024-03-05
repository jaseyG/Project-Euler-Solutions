# Project Euler 18

f = open('triangle18.txt', 'r')
file_list = f.readlines()
tri_visual = []
triangle = []
for i in file_list:
    tri_visual.append(i.replace('\n', ''))
    
# Visualisation
for i in tri_visual:
   print(i.center(100))
print('')

for i in tri_visual:
    triangle.append(i.split(' '))
    
for n, i in enumerate(triangle):
    for n2, j in enumerate(i):
        triangle[n][n2] = int(j)

sums = []

for i, row in enumerate(reversed(triangle)):
    if i == 0:
        pass
    else:
        for j, value in enumerate(row):
            big = max(triangle[15 - i][j] + value, triangle[15 - i][j + 1] + value)
            sums.append(big)
        triangle[14 - i] = sums
        sums = []
        
print(triangle[0][0])