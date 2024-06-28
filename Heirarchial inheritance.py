class Human(object):
    def __init__(self,name,age):
        print("from human init")
        self.name=name
        self.age=age
    def showDetails(self):
        print(f"name:{self.name} and age:{self.age}")
    def eat(self):
        print("i can eat")
class Male(Human):
    def __init__(self,name,age,location):
        print("calling init form male class")
        Human.__init__(self,name,age)
        self.location=location

    def sleep(self):
        print("i can sleep whole day")
class Female(Human):
    def __init__(self,name,age,can_dance):
        print("calling init from female class")
        Human.__init__(self,name,age)
        self.know_dance=can_dance
    def showDetails_F(self):
        print(f"name:{self.name} and age:{self.age}")
    def work(self):
        print("i can work")
print("FROM FEMALE CLASS")
female_1=Female("sudheshna",20,"yes")
print(female_1.name)
print(female_1.age)
print(female_1.know_dance)
female_1.showDetails_F()
# female_1.eat()
print(" ")
print("FROM MALE CLASS")
male_1=Male("srujan",21,"kakinada")
# male_1.eat()
# male_1.sleep()
# female_1.showDetails()
print(male_1.name)
print(male_1.age)
print(male_1.location)
male_1.showDetails()