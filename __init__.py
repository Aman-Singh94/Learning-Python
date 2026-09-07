class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            print(self.name, "PASS")
        else:
            print(self.name, "FAIL")

# argument give in result in class and object.py
# but in it we give data in constructor and then we call result method without any argument

student1 = Student("Aman", 85)
student2 = Student("Rahul", 32)

student1.result()
student2.result()