#Project Euler 32

from time import time

start = time()

ones_dict = { "1" : ["3","7"],
              "2" : ["3","4","6","7","8","9"],
              "3" : ["7","9"],
              "4" : ["2","3","6","7","8","9"],
              "5" : [],
              "6" : ["2","3","4","7","8","9"],
              "7" : ["3","9"],
              "8" : ["2","3","4","6","7","9"],
              "9" : [],
              "0" : [] }





##for i in range(1,10):
##    for j in range(i,10):
##        dig = [i,j,0]
##        if i != j and  i*j % 10 not in dig:
##            print(i, "x", j, "=", i*j % 10)
##
##print (ones_dict["4"])

pan = []

for num in range(1000,100000):
    for div in range(2,100):
        if num % div == 0:
            chars = str(num) + str(div) + str(num//div)
            #print(chars)
            if len(chars) == 9:
                digits = []
                for char in chars:
                    if char not in digits:
                        digits.append(char)
                if len(digits) == 9 and "0" not in digits and num not in pan:
                    pan.append(num)
                    print(div, num//div, num)

total = 0

for num in pan:
    total += num
print(total)
print("Run in", time()-start)

start = time()

pan = []

for i in range (2,10):
    for j in range(1000,5000):
        if len(str(i*j)) == 4:
            chars = str(i*j) + str(i) + str(j)
            digits = []
            for char in chars:
                if char not in digits:
                    digits.append(char)
            if len(digits) == 9 and "0" not in digits and i*j not in pan:
                pan.append(i*j)
                print(i,j,i*j)


for i in range (10,100):
    for j in range(100,1000):
        if len(str(i*j)) == 4:
            chars = str(i*j) + str(i) + str(j)
            digits = []
            for char in chars:
                if char not in digits:
                    digits.append(char)
            if len(digits) == 9 and "0" not in digits and i*j not in pan:
                pan.append(i*j)
                print(i,j,i*j)

total = 0

for num in pan:
    total += num
print(total)
print("Run in", time()-start)
            
