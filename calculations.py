#Prime Checker
def prime_checker(x):
    y = 3
    if x % 2 == 0:
        return False
    
    while y < x/2:
        if x % y != 0:
            y += 2
       
        else:
            return False
        
    return True
            
#Palindrome Checker
def palindrome_checker(x):
    n = len(str(x)) - 1
    xString = str(x)
    a = 0
    
    b = n
      
    while a < b:
        if xString[a] == xString[b]:
            a += 1
            b -= 1
        else:
            return False
    return True
    
def prime_finder(limit): # sieve of eratosthenes
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while p**2 <= limit:
        if sieve[p]:
            for i in range(p**2, limit + 1, p):
                sieve[i] = False
        p += 1
    return [i for i in range(limit + 1) if sieve[i]]

# UNFINISHED
def grid_product(grid, size):
    try:
        size = int(input('Enter the number of adjacent values you would like to multiply: '))
    except:
        print('Invalid')
        grid_product(grid.txt, size)
        
    f = open(grid.txt, 'r')
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
    
    x = len(grid2)
    y = len(grid2[0])
    product = []
    
    # Horizontal
    for row in grid2:
        for i, value in enumerate(row):
            if i <= (y - 1) - size:
                product.append(value * row[i + 2])
    
    
    # Vertical
    
    
    
    # Diagonal Top-Left to Bottom-Right
    
    
    
    # Diagonal Bottom-Left to Top-Right
    
    
def triangle_num_gen(term):
    current = []
    base = 0
    for j in range(term):
        for i in range(term + 1):
            current.append(base + 1)
            base = i
            base = sum(current)
            current = []
    return int(base / 2)

def fibonacci(n):
    lst = [1, 1]
    x = 0
    y = 1
    for i in range(0, n  - 2):
        lst.append(lst[x] + lst[y])
        x = y
        y += 1
    return lst[len(lst) - 1]
        