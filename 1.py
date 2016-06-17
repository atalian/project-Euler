#Project Euler 1

from time import time

start = time()

total = 0

for i in range(1001):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print (total)
print ("Run in", time() - start)
