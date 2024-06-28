# s='''ai 'is' \"our\" \'next\" future'''
# print(s)
# a='''sudheshna
# software
# engineer'''
# print(a)
# a='''sudhesh\na
# software
# engineer'''
# # print(a)
# a='''sudhesh\ta
# software
# engineer'''
# print(a)
##STRING INDEXING
# s="machine learning is a method in ai"
# print(s[1])
# print(s[-4])
##print(s[34]) ## index out of range error
# string1=input("enter some string:")  ##hello
# neg=-(len(string1))
# for i in range(0,len(string1)):
#     print(f"the character at positive index {i} at and negative index {neg} is {string1[i]}")
#     neg=neg+1
s="python is very useful in machine learning"
# print(s[0:len(s)+1:1])
# print(s[4:23:3])
# print(s[::])
# print(s[:100:])
# print(s[len(s):0:-1])
# print(s[20:4:-1])
# s="python"
# l="language"
# print(s+" "+l)
# print(s*3)
# ## MEMBERSHIP
# print('y' in s)
# print('k' not in s)
# print('s'  in l)
# string=input("enter a sting:")
# substr=input("enter a substring:")
# if substr in string:
#     print(f"{substr} is present in {string}")
# else:
#     print(f"{substr} is not present in {string}")
# s="python is great language for machine learning"
# i=0
# while i<len(s):
#     print("forword direction:")
#     for i in range(0,len(s)):
#         print(s[i],end="")
#     print(" ")
#     rev=s[::-1]
#     print("backward direction:")
#     print(rev)
#     i+=1
h="pyhton is the best"
print("forward direction:")
for i in h:
    print(i,end="")
print(" ")
print("forward direction:")
for i in s[::]:
    print(i,end="")
print(" ")
print("backward direction:")
for i in s[::-1]:
    print(i,end="")
















