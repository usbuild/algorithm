from random import random

n = 10
data = [int(random() * 100) for x in range(0, n)]
print data

def select_sort(A):
    for i in range(0, len(A)):
        for j in range(i, len(A)):
            if A[i] < A[j]:
                A[i], A[j] = A[j], A[i]


select_sort(data)
print data