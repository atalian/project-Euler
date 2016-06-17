#Project Euler 5

from time import time

start = time()

i = 20

done = False

while not done:
    if all(not (i % j) for j in range(2,21)):
        done = True
    else:
        i += 20

print (i)
print ("Run in", time()-start)
