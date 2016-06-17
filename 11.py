#Project Euler 11

from time import time

start = time()

with open("11.txt","r") as file:
    table = [[int(num) for num in line.split()] for line in file]

maxp = 0

for row in table:
    for i in range(len(row)-3):
        prod = 1
        for j in range(4):
            prod *= row[i+j]
        maxp = max(maxp, prod)

for row in range(len(table)-3):
    for col in range(len(table[row])):
        prod = 1
        for j in range(4):
            prod *= table[row+j][col]
        maxp = max(maxp, prod)

for row in range(len(table)-3):
    for col in range(len(table[row])-3):
        prod = 1
        for j in range(4):
            prod *= table[row+j][col+j]
        maxp = max(maxp, prod)

for row in range(len(table)-3):
    for col in range(3, len(table[row])):
        prod = 1
        for j in range(4):
            prod *= table[row+j][col-j]
        maxp = max(maxp, prod)

print (maxp)
print ("Run in ", time()-start)
