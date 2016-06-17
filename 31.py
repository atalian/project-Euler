#Project Euler 31

from time import time

start = time()

denom = [1,2,5,10,20,50,100,200]

mem = [-1] * 11


total = 0
def change_num(n, mx):
    if n == 0:
        return 1
    else:
        valid = [change_num(n - val, val) for val in filter(lambda x: n - x >= 0 and x <= mx, denom)]
        return sum(valid)

#for i in range(1,10):
#    mem[i] = change_num(i,200)



print (change_num(200,200))
print ("Run in", time()-start)
