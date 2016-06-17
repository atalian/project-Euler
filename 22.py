#Project Euler 22

from time import time

start = time()

with open("22.txt", "r") as file:
    names = file.read().split("\",\"")
    names[0] = names[0][1:len(names[0])]
    names[len(names)-1] = names[len(names)-1][0:len(names[len(names)-1])-1]

    names.sort()

    total = 0

    for index, name in zip(range(len(names)), names):
        score = 0
        for char in name:
            score += ord(char) - 64
        total += score*(index+1)

print (total)
print ("Run in", time()-start)    
