class A:
    def display(self):
        print("display from A class")
class B(A):  ## single
    pass
    # def display(self):
    #     print("display from B class")
class C(A):
    def show(self):
        print("Hi from C class")
    # def display(self):
    #     print("display from C class")
class D(B,C):  ## multiple inheritance
    pass
    # def display(self):
    #     A.display(self)
    #     print("display from D class")

d1=D()
# d1.show()
d1.display()
# print(D.mro())