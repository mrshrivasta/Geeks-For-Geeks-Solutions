class myStack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, x):
        node = Node(x)
        node.next = self.top
        self.top = node
        self.count += 1

    def pop(self):
        if self.top is None:
            return

        self.top = self.top.next
        self.count -= 1

    def peek(self):
        if self.top is None:
            return -1
        return self.top.data

    def isEmpty(self):
        return self.top is None

    def size(self):
        return self.count