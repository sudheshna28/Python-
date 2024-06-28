# s="i am self learning person and i love learning"
# print(s.find("learning"))  ## smallest index
# print(s.rfind("learning"))  ## largest index
# print(s.index("a"))     ## smallest index
# print(s.rindex("a"))     ## largest index
# print(s.rfind("a"))
# # if the substring is not present in the main string find() returns -1 and index() throws error
# #print(s.find("k"))
# print(s.index("k"))
#   #COUNT()
# print(s.count("learning",10,30))
#  # COMPARING STRINGS
# s1=input("enter first string:")
# s2=input("enter second string:")
# if s1>s2:
#     print(f"{s1} is greater than {s2}")
# elif s1==s2:
#     print(f"{s1} and {s2} are equal")
# else:
#     print(f"{s1} is less than {s2}")
#
#     ## STRIP()
# s=input("enter your city name:")
# s=s.strip()  ## lstrip(),strip()
# if s=="hyderabad":
#     print("hello!! hyderabadii")
# elif s=="kakinada":
#     print("hello!! Andhrawala")
# else:
#     print("invalid city name")
#
#    #EXERCISE
# main_string=input("enter a string:") ##hello
# sub_string=input("enter a sub string:") ##l
# flag=0
# while flag<len(main_string) :##5
# for i in range(0,len(main_string)):
#     if main_string[i]==sub_string:
#         print("found at position:",i)
#     elif i <len(main_string):
#         continue
#     else:
#         break
#
#  # REPLACE()
# s="python is very difficult"
# s1=s.replace("difficult","easy")
# print(s1)
# str="abababababbaba"
# s1=str.replace("b","a")  ## replace every occurance of b
# print(s1)
# print("id of str is:",id(str))
# print("is of s1 is:",id(s1))  ## a new object will be created because of immutability nature of string
#
#   # split()
# s="python academy"
# print(s.split())
# s="20-9-2020"
# print(s.split("-"))
# h=s.split("-")
# for i in h:
#     print(i,end=" ")
#
#
# #    #JOIN()
# s=["pani puri","chat","samosa","noodles","jalebi","pizzaa"]
# print("*".join(s))

# s="Kakinada Has the Most Beautiful beach Ever"
# s_lower=s.lower()
# print(s_lower)
# s_upper=s.upper()
# print(s_upper)
# s_title=s.title()
# print(s_title)   ## first character in every word
# s_capitalize=s.capitalize()
# print(s_capitalize)  ## first character in whole sentence
# s_swapcase=s.swapcase()
# print(s_swapcase)

## endswith and starts with
# s="machine learning is a technique used in ai to make machine learn from data to act intelligent"
# print(s.endswith("machine"))
# print(s.endswith("intelligent"))
# print(s.startswith("machine"))
# print(s.startswith("technique"))

## type of characters present in the string
# print("deeplearning".isalpha())
# print("728787232344".isdigit())
# print(" ".isspace())
# print("sudheshna28".isalnum())
# print("hajsjh".islower())
# print("JSJHSJJAH".isupper())
# print("Kakinada Hyderabadii".istitle())
# print("a".isalnum())

s=input("Enter any character:")
if s.isalnum():
    print("Alpha Numeric Character")
    if s.isalpha():
        print("Alphabet character")
        if s.islower():
            print("Lower Case Alphabet Character")
        elif s.isupper():
            print("Upper Case Alphabet Character")
        elif s.istitle():
            print("Title Case character")
        elif s.isdigit():
            print("Digit Character")
else:
    print("it is a space character")






























