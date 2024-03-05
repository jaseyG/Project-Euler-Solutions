# Project Euler 27
from euler import calculations as c

prime_dict = {}
consecutive = 0
n = 0

b_list = []
for b in range(1, 1000):
    if c.prime_checker(b):
        b_list.append(-b)
        b_list.append(b)
        
breaker = False
for a in range(- 999, 1000):
    for b in b_list:
        breaker = False
        while breaker == False:
            if c.prime_checker(abs(n**2 + a*n + b)):
                consecutive += 1
                n += 1
            else:
                prime_dict[f'a = {a}, b = {b}'] = consecutive
                consecutive = 0
                n = 0
                breaker = True


key_list = list(prime_dict.keys())
value_list = list(prime_dict.values())
print(key_list[value_list.index(max(value_list))])
