#Project Euler 40

from time import time

start = time()

digits = []

num = 1
count = 1

while len(digits) < 6:
    num += 1
    count += len(str(num))
    if count >= 10**(len(digits)+1):
        digits.append(str(num)[-(count-10**(len(digits)+1))-1])

prod = 1

for i in digits:
    prod *= int(i)

print(prod)
print("Run in", time()-start)
