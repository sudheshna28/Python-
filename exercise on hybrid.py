class University:
    def __init__(self):
        self.uni_name="ADITYA"
    def showDetails(self):
        print(f"the name of university is:{self.uni_name}")

class Course(University):
    def __init__(self):
        University.__init__(self)
        self.course_name="python"
    def showDetails(self):
        print(f"the course taught in {self.uni_name} is {self.course_name}")

    def work(self):
        print("in course class")


class Branch(University):
    def __init__(self):
        University.__init__(self)
        self.branch_name="aiml"
    def showDetails(self):
        print(f"the branch name in the {self.uni_name} is {self.branch_name}")
    def work(self):
        print("in branch class")


class Student(Course,Branch):
    def __init__(self):
        Branch.__init__(self)
        Course.__init__(self)
        University.__init__(self)
        self.stu_name="Sudheshna"
    def showDetails(self):
        print(f"Hello my name is {self.stu_name} and i m from {self.branch_name} learning {self.course_name} from the university {self.uni_name}")
    def work(self):
        super().work()
        print("hello")


class Faculty(Branch):
    def __init__(self):
        Branch.__init__(self)
        University.__init__(self)
        self.faculty_name="Divya"
    def showDetails(self):
        print(f"my name is: {self.faculty_name} and i m from the branch: {self.branch_name} and in the university: {self.uni_name}")


fac_1=Faculty()
Faculty.showDetails(fac_1)
stu_1=Student()
Student.showDetails(stu_1)
Branch.showDetails(fac_1)
Course.showDetails(stu_1)
University.showDetails(fac_1)
stu_1.work()