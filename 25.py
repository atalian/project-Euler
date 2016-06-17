#Project Euler 25

from time import time

start = time()

current = 1
prev = 1
nth = 2

digits = 0

while digits < 1000:
    temp = current
    current = current + prev
    prev = temp
    digits = len(str(current))
    nth += 1

print (nth)
print ("Run in", time()-start)
