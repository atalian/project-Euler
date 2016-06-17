#Project Euler 19

from time import time
import datetime

start = time()

first = datetime.date(1901, 1, 1)
last = datetime.date(2000, 12, 31)

sunday = datetime.date(1901, 1, 6)

num = 0

while sunday <= last:
    if sunday.day == 1:
        num += 1

    sunday = sunday.fromordinal(sunday.toordinal()+7)

print (num)
print ("Run in", time()-start)
