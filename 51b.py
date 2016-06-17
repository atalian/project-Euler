#Project Euler 51

from time import time
#from bisect import index

start = time()

lim = 1000

primes = [0] * lim
prime = 0

cur = 2
num = 2
p = []
ma = 0

while cur < lim:
    if primes[cur] == 0:
        num = 2*cur
        while num < lim:
            primes[num] = 1
            num += cur
    cur += 1
    
for j in range(2,lim):
    if primes[j] == 0:
        p.append(j)

#p = list(filter(lambda x: x > 100000, p))
print(p)

def sub(num, rep, digits):
    s = str(num)
    for index in digits:
        if int(index) > len(s):
            return "error"
        s = s[0:int(index)-1] + str(rep) + s[int(index): ]
    return int(s)



def for_perm(perm):
    print("substititue digit(s)", perm)
    ma = 0
    if len(str(perm)) == 1:
        for prime in p:
            count = 0
            works = []
            for k in range(10):
                if (10-k) + count < 8:
                    break
                if sub(prime, k, perm) in p:
                    count += 1
                    works.append(k)
                    if count > ma:
                        ma = count
                        print(prime, works)

def perm(num, left, m):
    if len(num) == m:
        for_perm(num)
    else:
        for i in range(len(left)):
            #print(num, left, i)
            num += left.pop(0)
            perm(num, left[:], m)
            #left.insert(i, num[-1])
            num = num[:-1]
        #return num
    
digits = [str(i) for i in range(1,len(str(lim)))]

#print(index(p, 11))

for i in range(1,len(digits)):
    #print("i =", i)
    #perm("", digits[:], i)
    pass



#print(sub(3094093, 7, "143"))





print("Run in", time()-start)
