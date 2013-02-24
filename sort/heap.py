from random import random
n = 10
data = [int(random() * 100) for x in range(0, n) ]

print data
def heapify(d, i):
    l = i * 2
    r = i * 2 + 1

    if l < len(d) and d[l] > d[i]:
        largest = l
    else:
        largest = i

    if r < len(d) and d[r] > d[largest]:
        largest = r

    try:
        largest
    except NameError:
        largest = None

    if largest is not None and largest != i:
        d[i], d[largest] = d[largest], d[i]
        heapify(d, largest)

def build_heap(d):
    i = int(len(d) / 2)
    while i >= 0:
        heapify(d, i)
        i -= 1

output = []

def heap_sort(d):
    build_heap(d)
    i = len(d) - 1
    while i > 0:
        output.append(d[0])
        d[0] = d.pop(i)
        heapify(d, 0)
        i -= 1
    output.append(d[0])

heap_sort(data)
print output
