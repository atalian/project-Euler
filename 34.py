#Project Euler 34

from time import time

start = time()

fact_dict = { "0" : 1,
              "1" : 1,
              "2" : 2,
              "3" : 6,
              "4" : 24,
              "5" : 120,
              "6" : 720,
              "7" : 5040,
              "8" : 40320,
              "9" : 362880 }

def sum_fact(n):
    total = 0
    for char in str(n):
        total += fact_dict[char]
    return total

nums = []
for num in range(10,10000000):
    if num == sum_fact(num):
        nums.append(num)

print(nums)
print("Run in", time()-start)
