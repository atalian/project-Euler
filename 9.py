#Project Euler 9

from time import time

start = time()


for i in range(1,1000):
    for j in range(1,1000-i):
        c = 1000-i-j
        if i**2 + j**2 == c**2:
            print (i*j*c)
            break
        else:
            continue
        break
    else:
        continue
    break

print ("Run in", time()-start)
