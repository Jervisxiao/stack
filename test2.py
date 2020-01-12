import X
import Y


class Stack(Z):
    x = X()
    y = Y()
    
    def __init__(self):
        self.items = []

    def is_Empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def stack_1(self):
        self.a.a_1()
        self.b.b_1()

    def stack_2(self, num):
        self.x_1(num)
        self.x.y_2()
        self.y_2()
