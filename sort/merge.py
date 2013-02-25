from random import random

n = 10
data = [int(random() * 100) for x in range(0, n)]
print data


def merge(A, p, q, r):
    L = A[p:q]
    R = A[q:r]

    j = k = 0
    for i in range(p, r):
        if j == len(L):
            A[i] = R[k]
            k += 1
            continue

        if k == len(R):
            A[i] = L[j]
            j += 1
            continue

        if L[j] > R[k]:
            A[i] = R[k]
            k += 1
        else:
            A[i] = L[j]
            j += 1


def merge_sort(A, p, r):
    if p < r - 1:
        q = int((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q, r)
        merge(A, p, q, r)


merge_sort(data, 0, len(data))
print data