class instructor:
    def __init__(self,name,address):
        self.ins_name=name
        self.ins_address=address
        self.followers=0

instructor1=instructor("payal","kakinada")
print("Instructor 1 details:")
print(instructor1.ins_name)
print(instructor1.ins_address)


instructor2=instructor("sudhi","hyderabad")
print("Instructor 2 details:")
print(instructor2.ins_name)
print(instructor2.ins_address)

instructor3=instructor("keerthi","vizag")
print("Instructor 3 details:")
print(instructor3.ins_name)
print(instructor3.ins_address)

instructor4=instructor("srujan","guntur")
print("Instructor 4 details:")
print(instructor4.ins_name)
print(instructor4.ins_address)