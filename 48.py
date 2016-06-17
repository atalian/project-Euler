#Project Euler 48

from time import time

start = time()

total = 0
for i in range(1,1000):
    total += ((i**i) % 10000000000)

print(total % 10000000000)
print("Run in", time()-start)
