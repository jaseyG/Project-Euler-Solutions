# Project Euler 15

import random
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wlexpr, wl
session = WolframLanguageSession()


def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product += i
    return product

movement = ['r', 'd']
size = 8
paths = []

def create_unique_path(movement, size):
    current_path = []
    for i in range(1, size * 2 + 1):
        if current_path.count('r') == size:
            current_path.append(movement[random.randint(1, 1)])
        elif current_path.count('d') == size:
            current_path.append(movement[random.randint(0, 0)])
            
        else:
            current_path.append(movement[random.randint(0, 1)])
        
    if current_path in paths:
        #create_unique_path(movement, size)
        pass
    else:
        paths.append(current_path)
        
for i in range(1000000):
    create_unique_path(movement, size)
    
print(len(paths))

# Here I put the pattern into Wolfram Alpha and it successfully identified the pattern. However, for some reason, Mathematica does not.

    
outcomes = [6, 20, 70, 252, 924, 3432]
        #   2  3   4    5    6
expression = wlexpr('{6, 20, 70, 252, 924, 3432}')
#pattern = session.evaluate(wl.FindSequenceFunction(expression))
#result = session.evaluate(wlexpr(f'{pattern}[22]'))
#print(result)



