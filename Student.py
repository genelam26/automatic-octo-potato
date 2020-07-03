class Student:

    def __init__(self,name,major,gpa,is_Honors):
        self.name=name
        self.major=major
        self.gpa=gpa
        self.is_Honors=is_Honors
    def to_String(self):
        if(self.is_Honors):
            return self.name+" "+self.major+" "+str(self.gpa)+" "+"Honors"
        else:
            return self.name+" "+self.major+" "+str(self.gpa)+" "+"not Honors"
    # inheritance
    def pay_Tuition(self):
        print("Paid tuition")
    def enroll_in_Classes(self):
        print("enrolled in classes")
    def dropout(self):
        print("Dropped out")
