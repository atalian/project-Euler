#Project Euler 35

from time import time

start = time()

def is_prime(n):
    if n in primes:
        return True
    else:
        return all(n % prime for prime in filter(lambda p: p <= n**0.5, primes))

def is_circ(n):
    return all(is_prime(int(str(n)[-i:]+str(n)[:-i])) for i in range(len(str(n))))

primes = [2]

for i in range(3,1000,2):
    if all(i % prime for prime in filter(lambda p: p <= i**0.5, primes)):
        primes.append(i)

digits = [0,1,3,7,9]
circ = []
for hunthou in digits:
    for tenthou in digits:
        for thou in digits:
            for hun in digits:
                for tens in digits:
                    for ones in range(1,10,2):
                        num = max(hunthou, 0)*100000 + max(tenthou, 0)*10000 + max(thou, 0)*1000 + \
                              max(hun, 0)*100 + max(tens, 0)*10 + ones
                        if is_circ(num):
                            circ.append(num)
print(len(circ))
print("Run in", time()-start)
