#Project Euler 26

from time import time

start = time()

div = 0
maxnum = 0
for i in filter(lambda x: x % 5, range(3,1000,2)):
    exp = 1
    while not (10**exp % i == 1):
        exp += 1
    if exp > maxnum:
        maxnum = exp
        div = i
print (div)
print ("Run in", time()-start)
