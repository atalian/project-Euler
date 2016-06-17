#Project Euler 42

from time import time

start = time()

def word_val(word):
    total = 0
    for char in word:
        total += ord(char) - 64
    return total

with open("42.txt", "r") as file:
    words = file.read().split("\",\"")
    words[0] = words[0][1:len(words[0])]
    words[len(words)-1] = words[len(words)-1][0:len(words[len(words)-1])-1]

    m = 0
    for word in words:
        if len(word) > m:
            m = len(word)

    triangles = []

    n = 1
    while n*(n+1)*0.5 <= m*26:
        triangles.append(int(n*(n+1)*0.5))
        n += 1

    tri_words = 0
    for word in words:
        if word_val(word) in triangles:
            tri_words += 1

    print(tri_words)
    print("Run in", time()-start)
