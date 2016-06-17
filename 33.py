#Project Euler 33

from time import time
from fractions import Fraction

start = time()

nums = []
denoms = []

for num in range(10,100):
    for den in range(num+1,100):
        if (den % 10) != 0 and (num % 10) == (den // 10) and num / den == (num // 10) / (den % 10):
            nums.append(num)
            denoms.append(den)

num = 1
den = 1

for i,j in zip(nums,denoms):
    num *= i
    den *= j

print(num,den)

print(Fraction(num,den))
print("Run in", time()-start)
