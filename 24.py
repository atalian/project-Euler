#Project Euler 24

from time import time

start = time()

def fact(n):
    prod = 1
    for i in range(2,n+1):
        prod *= i
    return prod

def lexic(num, nth):
    string = ""
    digits = [x for x in range(num)]
    for i in reversed(range(1,num)):
        place = int(nth / fact(i))
        string = string + str(digits[place]) 
        digits.remove(digits[place])
        nth = nth % fact(i)
    string = string + str(digits[0]) 
    return string

print (lexic(10,999999))
print ("Run in", time()-start)
