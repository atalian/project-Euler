#Project Euler 45

from time import time

start = time()


def pent(n):
    return n*(3*n-1)//2

def hexa(n):
    return n*(2*n-1)



pent_ind = 1
hex_ind = 143
searching = True

while searching:
    hex_ind += 1
    cur = hexa(hex_ind)
    while pent(pent_ind) < cur:
        pent_ind += 1
    else:
        if pent(pent_ind) == cur:
            searching = False

    

print(cur)
print("Run in", time()-start)
