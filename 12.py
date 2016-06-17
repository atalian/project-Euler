#Project Euler 12

from time import time

start = time()

def div_num(n):
    num = 1
    square = (int(n**0.5) == n**0.5)
    for i in range(2,int(n**0.5 +1)):
        if n % i == 0:
            num +=1
    if square:
        return 2*num-1
    else:
        return 2*num

def f_div():
    i = 1

    while True:
        if div_num((i*(i+1))/2) > 500:
            return i
        i += 1

num = f_div()
print ((num*(num+1))/2)
print ("Run in", time()-start)
