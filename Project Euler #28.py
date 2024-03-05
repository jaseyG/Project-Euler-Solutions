# Project Euler 28

def find_diagonal(size):
    down_right = []
    down_left = []
    up_left = []
    up_right = []
    i = 0
    start = 1
    
    for n in range(0, size):
        i = n
        increase = i * 8 + 2
        diff = (i + 1) * 2
       
        down_right.append(start + increase)
        down_left.append(down_right[n] + diff)
        up_left.append(down_left[n] + diff)
        up_right.append(up_left[n] + diff)
        start = down_right[n]
    
    return sum(down_right) + sum(down_left) + sum(up_left) + sum(up_right) + 1

print(find_diagonal(500))
    