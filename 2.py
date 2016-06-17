#Project Euler 2

from time import time

start = time()

current = 1
prev = 1
total = 0

while current <= 4000000:
    if current % 2 == 0:
        total += current

    oldcurrent = current
    current = current + prev
    prev = oldcurrent

print (total)
print ("Run in", time()-start)
