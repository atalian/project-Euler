#Project Euler 23

from time import time

start = time()

def is_abun(num):
    total = 1
    offset = 1
    if int(num**0.5) == num**0.5:
        total += int(num**0.5)
        offset = 0
        #print(num)
    for i in range(2, int(num**0.5)+offset):
        if num % i == 0:
            total += i + num // i
            #print (total)
            if total > num:
                return True
    
    return False

abun = []

for i in range(12, 28124):
    if is_abun(i):
        abun.append(i)

abun_sum = [False] * 28124

for i in range(len(abun)):
    for j in range(i, len(abun)):
        ijsum = abun[i]+abun[j]
        if ijsum < len(abun_sum):
            abun_sum[ijsum] = True
            continue
        break

total = 0
for i in range(len(abun_sum)):
    if abun_sum[i] == False:
        total += i

print(total)
print("Run in", time()-start)
