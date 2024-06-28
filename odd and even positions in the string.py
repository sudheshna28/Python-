# str=input("Enter a String:")
# print("Characters at even position")
# for i in range(0,len(str),2):
#     print(str[i],end=",")
# print(" ")
# print("Character at odd postion")
# for i in range(1,len(str),2):
#     print(str[i],end=",")

str=input("enter a string:")
even=""
odd=""
l=0
for i in str:
    if l%2==0:
        even=even+str[l]
    else:
        odd=odd+str[l]
    l=l+1
print("even position values are:",even)
print("odd position values are:",odd)