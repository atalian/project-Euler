#Project Euler 34

from time import time

start = time()

def is_pal(s):
    return s == s[::-1]

pals = []

for num in range(1,1000000):
    if is_pal(str(num)) and is_pal(bin(num)[2:]):
        pals.append(num)

total = 0
for num in pals:
    total += num

print(total)
print("Run in", time()-start)


