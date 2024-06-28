# str=input("enter a string:")
# output=("")
# alph,num="",""
# for i in str:
#     if i.isalpha():
#         alph=alph+i
#     else:
#         num=num+i
# output=sorted(alph)+sorted(num)
# for i in output:
#     print(i,end=",")

# str=input("enter a string:")
# output=""
# alph=""
# for i in str:
#     if i.isalpha():
#         output+=i
#         alph=i
#     else:
#         output=output+chr((ord(alph)+int(i)))
# print(output)

str=input("enter a string:")
output=""
alph=""
for i in str:
    if i.isalpha():
        output+=i
        alph=i
    else:
        output=output+chr((ord(alph)+int(i)))
print(output)