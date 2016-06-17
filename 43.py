#Project Euler 43

from time import time

from itertools import permutations

start = time()

nums = "0123456789"

total = 0

for perm in permutations(nums):
    
    perm = "".join(perm)
    #print(perm[1:4], perm[7:], perm)
    if int(perm[7:]) % 17 == 0 and \
       int(perm[6:9]) % 13 == 0 and \
       int(perm[5:8]) % 11 == 0 and \
       int(perm[4:7]) % 7 == 0 and \
       int(perm[3:6]) % 5 == 0 and \
       int(perm[2:5]) % 3 == 0 and \
       int(perm[1:4]) % 2 == 0:
        total += int(perm)

print(total)
print("Run in", time()-start)
