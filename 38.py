#Project Euler 38

from time import time

start = time()

def is_mult_pan(n):
    s = str(n)
    mult = 2
    while len(s) < 9:
        s += str(mult*n)
        mult += 1
    if len(s) == 9 and all(str(i) in s for i in range(1,10)):
        return int(s)
    else:
        return 0

m = 0

for i in range(192,10000):
    n = is_mult_pan(i)
    if n > m:
        m = n

print(m)
print("Run in", time()-start)

