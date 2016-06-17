#Project Euler 49

from time import time

start = time()

def is_prime(n):
    return all(n % i for i in range(3, int(n**0.5)+1, 2))

def is_perm(n, of): #not true perm check
    s = str(n)
    o = str(of)
    return all(i in o for i in s) and all(i in s for i in o)

for i in range(1001,10000,2):
    for j in range(2,4500,2):
        if i + 2*j > 9999:
            break
        if is_perm(i, i+j) and is_perm(i, i + 2*j) \
           and is_prime(i) and is_prime(i+j) and is_prime(i + 2*j):
            print(str(i)+str(i+j)+str(i + 2*j))

print("Run in", time()-start)
