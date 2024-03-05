#Project Euler 10 using Sieve of Eratosthenes

from euler import calculations as c

primes = c.prime_finder(2000000)
print(sum(primes))

