from random import random

n = 10
data = [int(random() * 100) for x in range(0, n)]
print data

def bubble_sort(A):
    for i in range(0, len(A)):
        for j in range(i + 1, len(A)):
            if A[j] > A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]

bubble_sort(data)
print data