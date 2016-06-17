#Project Euler 41

from time import time

start = time()

def is_prime(n):
    if n % 2 == 0:
        return False
    return all(n % i for i in range(3, int(n**0.5)+1, 2))


def gen_perm(num, left,  val):
    if val > 0:
        return val
    elif len(left) == 0:
        if is_prime(int(num)):
            return int(num)
        else:
            return 0
    else:
        for i in reversed(range(len(left))):
            num += left.pop(i)
            val = gen_perm(num, left, val)
            left.insert(i, num[-1])
            num = num[:-1]
        return val

digits = [str(i) for i in range(1,8)]

print(gen_perm("",digits, 0))
print("Run in", time()-start)
