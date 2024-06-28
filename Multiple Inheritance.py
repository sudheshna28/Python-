class Human:
    def __init__(self,num_heart):
        print("calling init from human")
        self.num_eyes=2
        self.num_nose=1
        self.heart=num_heart
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class Male:
    def __init__(self,name):
        print("calling init from male")
        self.Male_name=name
    def flirt(self):
        print("i can flirt")
    def work(self):
        print("i can code")

class Boy(Human,Male):# # method resolution order
    def __init__(self,name,language,num_heart):
        Human.__init__(self,num_heart)
        Male.__init__(self,name)
        self.language=language
        # self.num_nose=2
    def sleep(self):
        print("I can sleep")
    def work(self):
        print("i can write")
    def display(self):
        print(f"Hi i am {self.Male_name} and i work on language {self.language}")
boy_1=Boy("srujan","python",1)
# human_1=Human(1)
boy_1.eat()
boy_1.flirt()
boy_1.work()
Male.work(boy_1)
print(Boy.mro())
print(boy_1.num_nose)
print(boy_1.num_nose)
print(boy_1.num_eyes)
print(boy_1.Male_name)
print(boy_1.language)
print(boy_1.heart)
boy_1.display()