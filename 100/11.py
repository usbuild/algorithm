class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

def maxDepth(root):
    if root is None: return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

def findMaxLength(root):
    if root is None: return 0
    return max (findMaxLength(root.left),
            max(findMaxLength(root.right), maxDepth(root.left) + maxDepth(root.right) + 1)
            )

print findMaxLength(Node(Node(Node(None, None), None), None))
