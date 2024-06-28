def add_new_student(name,roll_no,age,course):
    student_data.append({"name":name,
                               "roll_no":roll_no,
                                "age":age,
                                "course":course
                              })
    
student_data=[
    {
        "name":"ram",
        "roll_no":10,
        "age":23,
        "course":"python"
    },
    {"name":"mohan",
     "roll_no":11,
     "age":22,
     "course":"c++",
     "home":["hyderabad","kakinada"]  ##nested list in dict and dict in list
     }
]
add_new_student("shyam",22,18,"java")
print(student_data)
