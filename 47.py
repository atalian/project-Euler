#Project Euler 47

from time import time

start = time()

n = 1000000

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

def factors(n):
    f = []
    curi = 0
    while n > 1:
        curp = primes[curi]
        if n % curp == 0:
            n /= curp
            if not curp in f:
                f.append(curp)
        else:
            curi += 1
    return f

def four_cons():
    l = []
    num = 2
    while len(l) < 4:
        if len(factors(num)) == 4:
            l.append(num)
        else:
            l = []
        num += 1
    else:
        return l

primes = prime_list(n)

print(four_cons())
print("Run in", time()-start)
