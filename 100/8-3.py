
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

def reverse(root):
    prev = None
    current = root
    next = current.next
    while next is not None:
        current.next = prev    
        prev = current
        current = next
        next = current.next
    current.next = prev
    return current

t = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, None)))))))


c = reverse(t)
while c is not None:
    print c.value
    c = c.next

def cardcmp(s1, s2):
    pass
