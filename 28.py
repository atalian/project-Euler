#Project Euler 28

from time import time

start = time()

total = 1
num = 1
for i in range(3,1002,2):
    for j in range(4):
        num += (i-1)
        total += num

print (total)
print ("Run in", time() - start)
