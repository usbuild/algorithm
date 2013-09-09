def findSum(i, s):
     start = 0
     end = len(i) - 1
     while start < end:
        if i[start] + i[end] == s: return (i[start], i[end])
        elif i[start] + i[end] < s:
            start += 1
        else:
            while start > 0:
                if i[start] + i[end] > s:
                    start -= 1
            if start == 0:
                end -= 1
     return None

print findSum([1, 2, 3, 4, 11, 15], 15)
