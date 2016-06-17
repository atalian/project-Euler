#Project Euler 50

from time import time

start = time()

lim = 1000000

primes = [0] * lim
prime = 0

cur = 2
num = 2
p = []

while cur < lim:
    if primes[cur] == 0:
        num = 2*cur
        while num < lim:
            primes[num] = 1
            num += cur
    cur += 1
    
for j in range(2,lim):
    if primes[j] == 0:
        p.append(j)

total = 0
m = 0

for s in range(0,len(p),2):
    total = 0
    for i in p[0:s]:
        total += i
    if total in p and s > m:
        prime = total
        m = s
    elif total > lim:
        break
        

if m % 2 == 1:
    m += 1

span = m

max_span = 1
total = 0
while total < lim:
    total += p[max_span] + p[max_span+1]
    max_span += 2

while span < max_span:
    for beg in range(1, max_span - span +1):
        total = 0
        for i in p[beg:beg+span+1]:
            total += i
        if total in p and span > m:
            prime = total
            m = span
        elif total > lim:
            break
    span += 2
        
    
print(prime)
print("Run in", time()-start)
