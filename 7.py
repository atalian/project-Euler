#Project Euler 7

from time import time

start = time()

primes = [2]

count = 1

num = 3

while count < 10001:
    if all(num % prime for prime in primes):
        primes.append(num)
        count += 1
    num += 2



print (primes[count-1])
print ("Run in", time()-start)
