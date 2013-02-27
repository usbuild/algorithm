from random import random

n = 10
data = [int(random() * 100) for x in range(0, n)]
print data


def shell_sort(A):
    h = 1
    while h < len(A) / 3: h = h * 3 + 1
    while h >= 1:
        for x in range(h, len(A)):
            j = x
            while j >= h and A[j] > A[j - h]:
                A[j], A[j - h] = A[j - h], A[j]
                j -= h

        h /= 3

shell_sort(data)
print data
