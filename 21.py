#Project Euler 21

from time import time

start = time()

def d(num):
    total = 1
    offset = 1
    if int(num**0.5) == num**0.5:
        total += int(num**0.5)
        offset = 0  
    for i in range(2, int(num**0.5)+offset):
        if num % i == 0:
            total += i + num // i
    return total

amic = 0

array = [0 for num in range(10000)]
array[1] = -1

for i in range(2,10000):
    if array[i] == 0:
        div = d(i)
        if div < 10000 and array[div] == 0 and d(div) == i:
            if i != div:
                amic += i + div
            array[i]  =  1
            array[div] = 1

print (amic)
print ("Run in", time()-start)
