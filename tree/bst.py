class TreeNode:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.key = None
        self.data = None

    def is_leaf(self):
        return self.left is None and self.right is None


class BST:
    def __init__(self, root=None):
        self.root = root

    def in_order(self, func):
        if self.root is not None:
            if self.root.left is not None:
                BST(self.root.left).in_order(func)

            func(self.root)
            if self.root.right is not None:
                BST(self.root.right).in_order(func)

    def max(self):
        t = self.root
        if t is None: return None
        while t.right is not None:
            t = t.right
        return t

    def min(self):
        t = self.root
        if t is None: return None
        while t.left is not None:
            t = t.left
        return t

    def find(self, key):
        t = self.root
        if t is None: return None
        while t is not None:
            if key == t.key: return t
            if key > t: t = t.right
            else: t = t.left
        return None

    def remove(self, key):
        t = self.find(key)
        if t is None: return None
        if t.is_leaf():
            if t.parent is not None:
                if t.parent.left.key == key:
                    t.parent.left = None
                else:
                    t.parent.right = None
            else:
                self.root = None
        else:
            if t.left is not None:
                node = BST(t.left).max()
                node.parent.right = None

                if t.parent is not None:
                    if t.parent.left.key == key:
                        t.parent.left = node
                    else:
                        t.parent.right = node





    def insert(self, key):
        if self.root is None:
            self.root = TreeNode()
            self.root.key = key
        else:
            node = TreeNode()
            node.key = key
            t = self.root
            while t is not None:
                if key > t.key:
                    if t.right is None:
                        t.right = node
                        node.parent = t
                        return
                    t = t.right
                else:
                    if t.left is None:
                        t.left = node
                        node.parent = t
                        return
                    t = t.left

tree = BST()
tree.insert(9)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(1)

def p(node):
    print node.key

tree.in_order(p)
