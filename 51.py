#Project Euler 51

from time import time

start = time()

lim = 1000000

primes = [0] * lim
prime = 0

cur = 2
num = 2
p = []

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


p = list(filter(lambda x: x > 100000, p))

#pstart = list(filter(lambda x: x > 200000, p))



def sub(rep,dig1,dig2,num):
    #print(int(str(num)[0:dig1] + str(rep) + str(num)[dig1+1:dig2] + str(rep) + str(num)[dig2+1:]))
    return int(str(num)[0:dig1] + str(rep) + str(num)[dig1+1:dig2] + str(rep) + str(num)[dig2+1:])

def is_prime(n):
    return all(n % i for i in filter(lambda x: x <= n**0.5, p))

pdoub = []

for prime in p:
    s = str(prime)
    for char1 in range(len(s)):
        for char2 in range(char1+1, len(s)):
            if s[char1] == s[char2]:
                pdoub.append([char1,char2,prime])

pairs = []
for i in range(6):
    pairs.append([])
    for j in range(6):
        pairs[i].append([])

for item in pdoub:
    #print(pdoub[key][0],pdoub[key][1])
    pairs[item[0]][item[1]].append(item[2])

m = 6

for i in range(5):
    for j in range(i+1,6):
        print(len(pairs[i][j]))


for i in range(4):
    for j in range(i+1,5):
        for prime in pairs[i][j]:
            count = 0
            for k in range(10):
                #if (10-k)+count <9:
                #    break
                if sub (k,i,j,prime) in pairs[i][j]:
                    count += 1
                    if count >= m:
                        m = count
                        print(m,k,i,j,prime,sub(k,i,j,prime), "Found in", time()-start)





##for prime in pstart:
##    for i in range(len(str(prime))):
##        for j in range(i+1, len(str(prime))):
##            count = 0
##            for k in range(10):
##                if (10-k)+count < 8:
##                    break
##                elif sub(k,i,j,prime) in p:
##                #elif is_prime(sub(k,i,j,prime)):
##                    count += 1
##                    if count > m:
##                        m = count
##                        print(m,k,i,j,prime, "Found in", time()-start)

print("Run in", time()-start)
