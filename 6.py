#Project Euler 6

from time import time

start = time()

n = 100

total = 0

square_of_sum = ((n*(n+1))/2)**2


for i in range(1,n+1):
    total += i**2

print (square_of_sum - total)
print ("Run in", time()-start)
