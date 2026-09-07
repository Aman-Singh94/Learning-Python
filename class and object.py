class Student:

    def result(self, name, marks):
        print("Name:", name)
        print("Marks:", marks)

        if marks >= 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")


student1 = Student()
student2 = Student()

student1.result("Aman", 85)
print()
print() # I added this line to create a space between the two outputs
student2.result("Rahul", 32)