def findMaxSub(data):
    sum = 0
    prev = 0
    for x in data:
        prev += x
        if prev < 0:
            prev = 0
        elif prev > sum:
            sum = prev
    return sum
print findMaxSub([-1, 0, 5, -3, 10, -9, 12, -11, 12])
