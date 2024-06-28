## why inheritance??  Code reusability and maintainability
class Human:
    def __init__(self,num_heart):
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=num_heart
        # print("in init")
    def eat(self):
        print("I can Eat")
    def work(self):
        print("I can work")
class Male(Human):
    def __init__(self,name,heart):
        super().__init__(heart)
        self.male_name=name
        self.s_heart=heart
        print(self.male_name)
        print(heart)
    def Run(self):
        print("I can Run")
    def work(self):
        super().work()  ## both super class work() funciton  and this also executes
        print("I can code python")
    def display(self):
        print(f"hi i am {self.male_name} and i have {self.s_heart} heart")
obj_sub=Male("srujan",1)
# obj_sub.work()
# obj_sub.eat()
# obj_sub.Run()
# obj_sub.work()  ## overrding
# obj_super=Human(1)
#obj_super.work()
# print(obj_sub.num_eyes)
# print(obj_sub.num_nose)
# print(obj_sub.name)
# print(obj_sub.name)
#print(obj_sub.num_heart)
obj_sub.display()





