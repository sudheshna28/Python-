from functools import reduce
# list1=[1,2,3,4,5]
# list2=[3,4,5,7,6]
result=(lambda x,y:x+y)([1,2,3,4,5],[3,4,5,7,6])
print(result)
res=reduce(lambda x,y:x+y,result)
print("the addition of numbers in the list is:",res)
# res=reduce(lambda x,y:x+y,list1,list2))
# print(res)