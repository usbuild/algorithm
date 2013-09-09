def isPostOrder(inp):
    if len(inp) <= 1: return True
    split = 0
    pivot = inp[len(inp) - 1]
    while split < len(inp) - 2:
        if inp[split] < pivot:
            split += 1
        else: break
    left = inp[:split]
    right = inp[split:-1]
    for x in right:
        if x < pivot:return False
    return isPostOrder(left) and isPostOrder(right)

print isPostOrder([5, 7, 6, 9, 11, 10, 8])
print isPostOrder([7, 4, 6, 5])
