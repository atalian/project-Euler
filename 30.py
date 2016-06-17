#Proect Euler 30

from time import time

start = time()

def sum_fifth(num):
    total = 0
    for digit in str(num):
        total += int(digit)**5
    return total

l = []
for i in range(10,354294):
    
    if i == sum_fifth(i):
        l.append(i)

total = 0
for num in l:
    total += num

print (total)
print ("Run in", time()-start)
