import random

n = 100
data = [int(random.random() * 100) for x in range(0, n)]

i = 0
while i < n:
    j = i
    while j > 0:
        if data[j] > data[j - 1]:
            data[j], data[j - 1] = data[j - 1], data[j]
        else:
            break
        j -= 1
    i += 1
print data
