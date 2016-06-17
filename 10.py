#Project Euler 10

from time import time

start = time()

sieve = [0] * 1000000

num = 3
total = 2

while num < 2000000:
    if sieve[int(num / 2)] == 0:
        total += num
        i = int(num/2)
        while i < 1000000:
            sieve[i] = 1
            i += num
    num += 2

print (total)

print ("Run in", time() - start)
