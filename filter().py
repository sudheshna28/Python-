# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# def is_A_student(score):
#     return score > 75
# over_75 = list(filter(is_A_student, scores))
# print(over_75)
#  ## using lambda function
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# over_75 = list(filter(lambda x:x>75, scores))
# print(over_75)
 ## PALINDROMES
Names = ("tomato","malayalam","wow","book","civic","radar","level","chrome","cloth")
palindromes = list(filter(lambda word: word == word[::-1], Names))
print(palindromes)