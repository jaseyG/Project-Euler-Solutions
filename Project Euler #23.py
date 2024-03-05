# Project Euler 23
from time import perf_counter
start = perf_counter()
total = 0
def find_divisors(n):
    divisors = []
    for i in  range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            if n / i == i:
                divisors.append(int(i))
            elif n / i not in divisors or i not in divisors:
                divisors.append(int(i))
                divisors.append(int(n / i))
    try:
        divisors.remove(n)
    except:
        pass
    return sorted(divisors)

def is_abundant(n):
    if sum(find_divisors(n)) > n:
        return True
    else:
        return False
    
abundant_numbers = []
for i in range(1, 28124):
    if is_abundant(i):
        abundant_numbers.append(i)

sum_list = []
for n, a in enumerate(abundant_numbers):
    for b in abundant_numbers[n : len(abundant_numbers) - 1]:
        if a + b > 28123:
            break
        elif a + b not in sum_list:
            sum_list.append(a + b)
            
for i in range(1, 28124):
    if i not in sum_list:
        total += i
print(total)

end = perf_counter()
print(f'In {round(end - start, 2)} seconds')
            