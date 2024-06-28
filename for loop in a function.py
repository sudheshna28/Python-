def Addition(list_1):
    sum=0
    for i in list_1:
        sum+=i
    return sum
list1=list(int(input("enter a list:")))
result=Addition(list1)
print(result)
