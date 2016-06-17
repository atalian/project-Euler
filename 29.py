#Project Euler 29

from time import time

start = time()

def primes_up_to(num):
    primes = [2]
    for i in range(3, num+1):
        prime_num = 0
        while primes[prime_num] <= i**0.5:
            if i % primes[prime_num] == 0:
                break
            prime_num += 1
        else:
            primes.append(i)
    return primes

primes = primes_up_to(100)

def prime_fact(num, primes):
    factors = [0] * len(primes)
    prime_num = 0
    while num > 1:
        if num % primes[prime_num] == 0:
            num /= primes[prime_num]
            factors[prime_num] += 1
        else:
            prime_num += 1
    return factors

factorization = []
for a in range(2, 101):
    factors = prime_fact(a, primes)
    for b in range(2,101):
        if not ([i*b for i in factors] in factorization):
            factorization.append([i*b for i in factors])
print (len(factorization))
print ("Run in", time()-start)


