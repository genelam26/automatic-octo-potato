from Student import Student
class Teacher(Student):
    def grade_Student(self):
        print("Student graded")
    #This overrides student
    def pay_Tuition(self):
        print("Unable to pay for tuition")