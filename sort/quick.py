from random import random

n = 10
data = [int(random() * 100) for x in range(0, n)]
print data

def quick_sort(A, p, r):
    if p < r:
        q = part(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def part(A, p, r):
    i = p
    pivot = A[r]
    for j in range(p, r):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i

quick_sort(data, 0, n - 1)
print data