#Project Euler 44

from time import time

start = time()

min_dist = 10000

n = 2

max_n = 1

pents = []

while n*(3*n-1)/2 - (n-1)*(3*(n-1)-1)/2 <= min_dist:
    while max_n*(3*max_n-1)/2 < 2*n*(3*n-1)/2:
        pents.append(max_n*(3*max_n-1)//2)
        max_n += 1
        #print(pents)

    
    for j in range(1,n-1):
        if pents[n-1]-pents[j] in pents and pents[n-1]+pents[j] in pents:
            print(n-1,j,pents[n-1]-pents[j])
            min_dist = 1
    
    n += 1

print(min_dist)
print("Run in", time()-start)
