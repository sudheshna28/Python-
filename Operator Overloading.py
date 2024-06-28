# print(1+2)    ## integers
# # print("1"+"2")  ## string
# # print(int.__add__(3,5))
# # print(str.__add__("sudhu","sai"))
# class ComplexNumber:
#     def __init__(self,r,i):
#         self.real=r
#         self.imaginary=i
#     def __add__(self, other):  ## c1,c2
#        return str(self.real + other.real) + "+" + str(self.imaginary+other.imaginary )+ "i"
#
#
# c1=ComplexNumber(1,2)
# c2=ComplexNumber(4,6)
# print(c1+c2)
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self,other):
        if self.age>other.age:
            return True
        else:
            return False

p1=Person("sudhi",10)
p2=Person("keerthi",15)
if p1>p2:
    print(f"{p1.name} must pay the bill")
else:
    print(f"{p2.name} must pay the bill")













