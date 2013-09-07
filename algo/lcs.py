def lcs(d1, d2):
    if len(d1) == 0 or len(d2) == 0: return []
    if d1[0] == d2[0]: return [d1[0]] + lcs(d1[1:], d2[1:])
    else:
        t1 = lcs(d1[1:], d2)
        t2 = lcs(d1, d2[1:])
        if len(t1) > len(t2):
            return t1
        else:
            return t2

def get(a, x, y):
    if x <  0 or x >= len(a):return 0
    elif y < 0 or y >= len(a[x]): return 0
    return a[x][y]

def same(x, y):
    if x == y: return 1
    return 0

def direct(d, x, y):
    if x == 0 and y == 0: return None
    if x == 0: return (x, y - 1)
    if y == 0: return (x - 1, y)
    t1 = d[x][y - 1]
    t2 = d[x - 1][y]
    t3 = d[x - 1][y - 1]
    if t1 > t2 and t1 > t3: return (x, y - 1)
    if t2 > t1 and t2 > t3: return (x - 1, y)
    return (x - 1, y - 1)


def lcs2(d1, d2):
    m = []
    i = 0
    while i < len(d1):
        m.append([])
        j = 0
        while j < len(d2):
            if i == j == 0: m[i].append(same(d1[i], d2[j]))
            else: m[i].append(max(get(m, i - 1, j - 1) + same(d1[i], d2[j]),
                max(get(m , i - 1, j),
                    get(m, i, j - 1)
                    )))
            j += 1
        i += 1
    o = []
    i, j = len(d1) - 1, len(d2) - 1
    cur = m[i][j]
    while True:
       x = direct(m, i, j) 
       if x is None: 
           if cur == 1: o.insert(0, d1[i])
           break
       else:
        nex = m[x[0]][x[1]]
        if cur - nex == 1:
            o.insert(0, d1[i])
        i, j = x
        cur = nex
    return o
                

def lcstr(d1, d2):
    if len(d1) == 0 or len(d2) == 0: return []
    if d1[0] == d2[0]: 
        t1 = []
        for x in range(0, len(d1)):
            if x >= len(d2) or d1[x] != d2[x]: break
            else: t1.append(d1[x])
    else: 
        t1 = []
    t2 = lcstr(d1[1:], d2)
    t3 = lcstr(d1, d2[1:])
    if len(t1) > len(t2) and len(t1) > len(t3): return t1
    elif len(t2) > len(t1) and len(t2) > len(t3): return t2
    else: return t3


def lcstr2(d1, d2):
    m = []
    i = 0
    biggest = 0
    pos = None
    while i < len(d1):
        m.append([])
        j = 0
        while j < len(d2):
            if i == j == 0: m[i].append(same(d1[i], d2[j]))
            else: 
                x = get(m, i - 1, j - 1) + same(d1[i], d2[j]);
                if biggest < x: 
                    pos = i
                    biggest = x
                m[i].append(x)
            j += 1
        i += 1
    if biggest == 0: return []
    return d1[pos - biggest + 1 :pos + 1]

        
d1 = [0, 1]
d2 = [1, 2, 3, 5, 4, 5]
print lcstr2(d1, d2)
