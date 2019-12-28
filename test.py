from x import A
from y import B
import D


class C(D):
    a = A()
    b = B()

    def c_1(self):
        self.a.a_1()
        self.b.b_1()

    def c_2(self, num):
        self.c_1(num)
        self.b.b_2()

    def c_3(self, num):
        self.a_1(num)
        self.a.b_2()
        self.c_2()


