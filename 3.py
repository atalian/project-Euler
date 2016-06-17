#Project Eueler 3

from time import time

start = time()

num = 600851475143
largest = int(num**0.5)+1

fact = 0
i = 3

while num > 1:
    if num % i == 0:
        fact = i
        num /= i
    else:
        i += 2

print (fact)
print ("Run in", time()-start)
