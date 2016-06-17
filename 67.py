#Project Euler 67

from time import time

start = time()

triangle = []

file = open("67.txt", "r")

char = "ok"
row = 0

while char != "":
    triangle.append([])
    for entry in range(row+1):
        string = ""
        char = file.read(1)
        while char.isnumeric():
            string += char
            char = file.read(1)
        else:
            triangle[row].append(int(string))
    else:
        #print (triangle[row])
        row += 1


max_path = []

for i in range(100):
    max_path.append([])
    max_path[i] = [-1] * (i + 1)


for row in reversed(range(100)):
    for entry in range(row+1):
        if row == 99:
            max_path[row][entry] = triangle[row][entry]
        else:
            max_path[row][entry] = \
                triangle[row][entry] + max(max_path[row+1][entry], \
                                            max_path[row+1][entry+1])

print (max_path[0][0])
print ("Run in", time()-start)


file.close()
