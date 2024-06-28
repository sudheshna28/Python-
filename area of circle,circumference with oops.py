# class Math:
#     pi=3.14
#     def __init__(self,radius):
#         self.shape_radius=radius
#     def area_circle(self):
#         area=Math.pi*(self.shape_radius**2)
#         print("the area of  circle is %5.2f" %(area))
#     def circumference(self):
#         circum=2*Math.pi*self.shape_radius
#         print("the circumference of  circle is %5.2f" % (circum))
#
#
# cir_values=Math(23)
# cir_values.area_circle()
# cir_values.circumference()

class Rectangle:
    def __init__(self,length,width):
        self.len=length
        self.wid=width
    def area_rectangle(self):
        area=self.len*self.wid
        return area
obj1=Rectangle(2,4)
result=obj1.area_rectangle()
print(result)