#Project Euler 37

from time import time

start = time()

def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0 or n == 0 or n == 1:
        return False
    return all(n % i for i in range(3,int(n**0.5) +1, 2))

trunc = []

num = 11
while len(trunc) < 11:
    if all(is_prime(int(str(num)[:i])) for i in range(1, len(str(num))+1)) and \
       all(is_prime(int(str(num)[i:])) for i in range(1, len(str(num)))):
        trunc.append(num)
    num+=2

total= 0
for i in trunc:
    total += i
    print(i)
print(total)
print("Run in", time()-start)
