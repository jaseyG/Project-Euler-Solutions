# Project Euler 14

# Any number that can be expressed as some index of 2 will provide a very short chain. 

# Upper cap is 2^19, anything else is greater than 1 million

avoid = []
for i in range(20):
    avoid.append(2**i)

def check_power(num):
    if num in avoid:
        return True

chain = []
best = (1, 1)

def process(n):
    chain.append(n)
    if n == 1:
        return len(chain)
    elif n % 2 == 0:
        process(n/2)
    else:
        process(3*n + 1)

for i in range(1, 1_000_000):
    process(i)
    if len(chain) > best[0]:
        best = (len(chain), i)
    chain = []

print(best)
        
        
        
        