from random import random

n = 10
data = [int(random() * 20) for x in range(0, 10)]
#data = range(0, 10)
data.sort()
print data
def binary_search(A, a):
    p = 0
    q = len(A)
    while p < q:
        if A[p] == a:
            print "found"
            return
        if p == q - 1:
            print "not found"
            return
        d = (p + q) / 2
        if a >= A[d]: p = d
        else: q = d


binary_search(data, 10)


