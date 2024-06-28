def scoreOfString(s):
    ascii_values=[]
    difference=[]
    sum=0
    for i in s: ##hello
        ascii_values.append(ord(i))
        ##print(ascii_values)
    for j in range(len(ascii_values)-1):
        diff=ascii_values[j]-ascii_values[j+1]
        difference.append(abs(diff))
        ##print(difference)
    for k in difference:
        sum=sum+k
    return sum
s=input("enter the string:")
result=scoreOfString(s)
print(result)