class TwoStacks:
    def __init__(self, n=100):
        self.arr = [0] * n
        self.top1 = -1
        self.top2 = n

    def push1(self, x):
        if self.top1 + 1 < self.top2:
            self.top1 += 1
            self.arr[self.top1] = x

    def push2(self, x):
        if self.top1 + 1 < self.top2:
            self.top2 -= 1
            self.arr[self.top2] = x

    def pop1(self):
        if self.top1 == -1:
            return -1
        x = self.arr[self.top1]
        self.top1 -= 1
        return x

    def pop2(self):
        if self.top2 == len(self.arr):
            return -1
        x = self.arr[self.top2]
        self.top2 += 1
        return x