#Project Euler 17

from time import time

start = time()

total = 0

len_word = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]


tens = [0,0, 6, 6, 5, 5, 5, 7, 6, 6]

hundred = 7

for x in len_word:
    total += x

for i in range(20, 100):
    total +=  tens[i // 10]
    total += len_word[i % 10]

for i in range(100, 1000):
    total += len_word[ i // 100] + hundred
    if 0 < i % 100 < 20:
        total += 3 + len_word[i % 100]
    elif 20 <= i % 100 < 100:
        total += 3
        total +=  tens[(i // 10) - 10*(i // 100)]
        total += len_word[i % 10]

total += len("onethousand")


print (total)
print ("Run in", time()-start)
