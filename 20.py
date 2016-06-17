#Project Euler 20

from time import time

start = time()

prod = 1
total = 0

for i in reversed(range(1,100)):
    prod *= i
    #while prod % 10 == 0:
    #    prod /= 10

for char in str(prod):
    total += int(char)

print (total)
print ("Run in", time()-start)
