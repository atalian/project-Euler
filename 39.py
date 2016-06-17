#Project Euler 39

from time import time

start = time()

squares = {}

for i in range(1, 1000):
    squares[i**2] = i

n = len(squares)

right = [0]*1001


for i in range(1,n):
    for j in range(i,n):
        if i**2+j**2 in squares and squares[i**2+j**2]+i+j <= 1000:
            right[squares[i**2+j**2]+i+j] += 1

m = 0
ind = 0

for num, index in zip(right, range(len(right))):
    if num > m:
        m = num
        ind = index

print(ind)
print("Run in", time()-start)
