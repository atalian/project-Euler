#Project Euler 8

from time import time

start = time()

f = open("8.txt", "r")

number = ""
char =""

reading = True

while reading:
    char = f.read(1)
    
    if char.isnumeric():
        number += char
    elif char == "":
        reading = False

f.close()

m = 0

for i in range(len(number)-12):
    prod = 1
    for j in range(13):
        prod *= int(number[i+j])
        if prod > m:
            m = prod

print (m)
print ("Run in", time()-start)
