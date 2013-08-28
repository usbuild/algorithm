class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

root = Node(10, 
        Node(6, Node(4, None, None), Node(8, None, None)),
        Node(14, Node(12, None, None), Node(16, None, None))
        )

def handle(root):
    if root.left is not None:
        (lmax,lmin) = handle(root.left)
        lmax.right = root
        root.left = lmax
    else:
        lmin = root
        root.left = None

    if root.right is not None:
        (rmax,rmin) = handle(root.right)
        rmin.left = root
        root.right = rmin
    else:
        rmax = root
        root.right = None

    return (rmax, lmin)

(max,min) = handle(root)
current = max
while current is not None:
    print current.value
    current = current.left

print "==========="
current = min
while current is not None:
    print current.value
    current = current.right
