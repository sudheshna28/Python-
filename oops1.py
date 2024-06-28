# class computer:
#     def config(self):
#         print("i5,16gb,1TB")
# comp1=computer()
# comp2=computer()
# ## using class
# computer.config(comp1)
# computer.config(comp1)
# ## using object
# comp1.config()  ## config takes comp1 as parameter and self takes comp1
# comp2.config()


class computer:
    ## init is a constructor,no need to call it same as java
    def __init__(self,cpu,ram): ## A special method used to initialize variables
        print(cpu)
        print(ram)



    def config(self):
        print("i5,16gb,1TB")
comp1=computer("i5","16gb")
comp2=computer("ryzen","8gb")
## using object
comp1.config() ## config takes comp1 as parameter and self takes comp1
comp2.config()
