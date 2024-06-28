# f1=open("file_1.txt","x")  ## creating a new file
#
# f1=open("file_1.txt","r")  ## can not do anything in read mode as there is no content before

f1=open("file_1.txt","r+")
# print(f1.read())
f1.write("Hello python tutorials")
print(f1.tell())
f1.seek(0)
# print(f1.seek())
print(f1.read())
