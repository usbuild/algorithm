class MyStack:
    def __init__(self):
        self.data = []
        self.max = []
    def push(self, a):
        if len(self.max) == 0:
            self.max.append(0)
        elif self.data[self.max[len(self.max) - 1]] > a:
            self.max.append(self.max[len(self.max) - 1])
        else:
            self.max.append(len(self.max))
        self.data.append(a)
    def pop(self):
        self.max.pop()
        return self.data.pop()
    def min(self):
        return self.data[self.max[len(self.max) - 1]]

s = MyStack()
s.push(1)
s.push(3)
s.push(7)
s.push(5)
s.push(9)
s.pop()
print s.min()
