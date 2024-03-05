# Project Euler 24
from itertools import permutations
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

perms = [''.join(p) for p in permutations('0123456789')]
permutation_list = []
for perm in perms:
    permutation_list.append(int(perm))
    
print(permutation_list[999_999])
