## over loading  ## compile time polymorphism --> python does not support this
# class Demo:
#     # def add(self,a,b,c=0):   ## default arguments
#     #     return a+b+c
#     def add(self,*args):
#         total=0
#         for i in args:
#             total=total+i
#         return total
#     # def add(self,a,b,c):
#     #     return a+b+c
# d=Demo()
# print(d.add(3,4))
# print(d.add(4,5,6))
# print(d.add(2,9,10,3))
#
#   overriding: run time polymorphism must have same number of arguments
class Father:
    def sleep(self):
        print("father sleeping time is 10:00 PM TO 5:00 AM")
    def eat(self):
        print("eating")
class son(Father):
    pass
    def sleep(self):
        print("son sleeping time is 1:00 AM TO 9:00 AM")
        super().sleep()
ram=son()
ram.sleep()
ram.eat()












