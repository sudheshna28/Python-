class Instructor:
    followers=0  #class object variable
    def __init__(self,name,address):
        self.inst_name=name
        self.inst_address=address
        # self.followers=0
    def display(self,subject,hours):
         self.inst_subject=subject
         self.inst_hours=hours
         print(f"Hi!! i am {self.inst_name} and i teach {subject} for {self.inst_hours} hours in a week")
    def update_followers(self,followers_name):
        self.followers+=1


instructor1=Instructor("keerthi","hyderabad")
# print(instructor1.inst_name)
# print(instructor1.inst_address)
# print(instructor1.followers)
instructor1.display("python",15)
instructor1.update_followers("honey")
print(instructor1.followers)
print(" ")
instructor2=Instructor("honey","u.s.a")
# print(instructor2.inst_name)
# print(instructor2.inst_address)
# print(instructor1.followers)
instructor2.display("java",12)
instructor2.update_followers("keerthi")
print(instructor2.followers)