#Project Euler 27

from time import time

start = time()

def is_prime(n):
    if n < 2:
        return False
    elif n in primes:
        return True
    else:
        if n == 2 or n % 2 == 1 and all(n % i for i in range(3,int(n**0.5)+1,2)):
            primes.append(n)
            return True
        else:
            return False

primes = []

max_streak = 0
max_ab = [0,0]

for a in range(-999,1000):
    for b in range(-999,1000):
        streak = 0
        n = 0
        while is_prime(n**2 + a*n + b):
            streak += 1
            n += 1
        if streak > max_streak:
            max_ab = [a,b]
            max_streak = streak

print ("Pair is",max_ab, "with prime streak", max_streak)
print ("Run in", time()-start)
