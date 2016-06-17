#Project Euler 18

from time import time
from random import random
from random import seed

start = time()

triangle = []

file = open("18.txt", "r")

line = line = file.readline()

lnum = 0

while line != "":
    triangle.append([])
    for i in range(lnum+1):
        #print(3*i, 3*i+1)
        triangle[lnum].append(int(line[3*i:3*i+2]))
    #print (triangle[lnum])
    lnum +=1
    line = file.readline()
    
at = 0
total = 75
mtotal = 0
mseq = []

seed()

total += triangle[i][at]

for k in range(1000):
    seq = [0]
    for i in range(len(triangle)-1):
        #print (random())
        if random() < (float(triangle[i+1][at+1]/ float(triangle[i+1][at] + triangle[i+1][at+1]))):
            at +=1
        total += triangle[i+1][at]
        seq.append(at)
    else:
        if total > mtotal:
            mtotal = total
            mseq = seq
        at = 0
        total = 75

print(mtotal)
print(mseq)
print("Run in", time()-start)

file.close()
