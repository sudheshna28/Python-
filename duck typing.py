class Duck:
    def swim(self):
        print("I am a duck and I can swim")
    def speaks(self):
        print("Quack Quack")
class Dog:
    def swim(self):
        print("I am a dog and I can swim")
    def speaks(self):
        print("Woof Woof")

class Person:
    def speaks(self):
        print("blah blah blah")
class Demo:
    def display(self,obj):
        obj.swim()
        obj.speaks()
        print("Information Displayed")

d=Duck()
dog=Dog()
demo=Demo()
demo.display(dog)
demo.display(d)
p=Person()
demo.display(p)  ## error because person has no function swim
## THIS IS POSSIBLE BECAUSE OF DYNAMIC TYPING AS CLASSSES OF OBJECTS DOES NOT MATTER
## IF THE  OBJECT HAS THAT FUNCTION IRRESPECTIVE OF CLASS IT WILL BE CALLED


