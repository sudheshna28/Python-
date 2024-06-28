class Human(object):
    can_breath=True  ## class object variable
    def __init__(self,num_heart):
        print("init from human class")
        self.eyes=2
        self.heart=num_heart
        self.nose=1
    def eat(self):
        print("I can eat")
    def work(self):
        print("i can work")
class Male(Human):
    def __init__(self,name,num_heart):
        print("init from Male class")
        super().__init__(num_heart)
        self.name=name
        print("NOSE:",self.nose)
    def sleep(self):
        print("I can sleep whole day")
class Boy(Male):
    def __init__(self,name,can_dance,num_heart):
        print("init from Boy class")
        Male.__init__(self, name,num_heart)
        Human.__init__(self,num_heart)
        self.know_dancing=can_dance
    def work(self):
        super().work()
        Human.work(self)
        print("I can code")
boy_1=Boy("sudhi",True,1)
print("EYES:",boy_1.eyes)
# print(Boy.mro())
print("NAME:",boy_1.name)
print("HEART:",boy_1.heart)
print("CAN DANCE:",boy_1.know_dancing)
print(boy_1.can_breath)