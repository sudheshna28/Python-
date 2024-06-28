# n=int(input("enter the number of rows you want:"))
# for i in range(4):
#     for j in range(4):
#         print("*",end=" ")
#     print( )

n=int(input("enter the number of rows you want:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print( )

# n=int(input("enter the number of rows you want:"))  ##3
# k = 1
# for i in range(1,n+1):  ## 1-4,1,2,3
#     for j in range(1,k+1): ## 1 to 2 ## 1 to 4  ## 1 to 6
#         print("*",end=" ")
#     k+=2
#     print( )

# rows=int(input("enter the number of rows:"))
# for i in range(0,rows+1):
#     for j in range(0,rows-i-1):
#         print(" ",end=" ")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print(" ")