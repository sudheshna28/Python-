class person():
    def __init__(self,name,aadhar,college):
        self.name=name
        self.aadhar=aadhar
        self.college=college
    def display(self):
        print("name:",self.name,"aadhar:",self.aadhar,"college:",self.college)
class student(person):
    def __init__(self,name,aadhar,college,roll,branch):
        super().__init__(name,aadhar,college)
        self.roll=roll
        self.branch=branch
    def display(self):
        person.display(self)
        print("name:",self.name,"Adhar:",self.aadhar,"rool no:",self.roll,"college:",self.college,"branch:",self.branch)
a=student('bhavya',12345,"acet","4214","aiml")
a.display()

