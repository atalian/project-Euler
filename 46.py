#Project Euler 46

from time import time

start = time()

n = 10000

def prime_list(n):
    p = [0] * n
    primes = []
    cur = 2

    while cur < n/2:
        for i in range(2*cur, n, cur):
            p[i]=1

        cur += 1
        while p[cur]==1:
            cur += 1

    for i in range(2,n):
        if p[i]==0:
            primes.append(i)

    return primes

def odd_comp_list(n, primes):
    c = [0] * n
    comps = []
    
    for i in range(2, n, 2):
        c[i] = 1
    for prime in primes:
        c[prime] = 1
    for i in range(4,n):
        if c[i]==0:
            comps.append(i)

    return comps

primes = prime_list(n)
comps = odd_comp_list(n,primes)
doub_sq = [2 * i**2 for i in range(1, int((0.5*n)**0.5)+2)]

def gb_other(n):
    cur_p = 0
    cur_d = 0
    while primes[cur_p] < n:
        while primes[cur_p] + doub_sq[cur_d] <= n:
            if primes[cur_p] + doub_sq[cur_d] == n:
                return [True, primes[cur_p], doub_sq[cur_d]]
            else:
                cur_d += 1
        else:
            cur_p += 1
            cur_d = 0
    
    return False


for i in comps:
    if gb_other(i) == False:
        print(i)
        break



print("Run in", time()-start)
