from student_package.student import Student

student1 = Student(1001, "jack", "jack@gmail.com", 45.2)
student2 = Student(1002, "peter", "peter@gmail.com", 85.2)
student3 = Student(1003, "mark", "mark@gmail.com", 56.5)
Student.schoolName = "Global school"
Student.schoolAddress = "chennai"


student1.display_data()
student2.display_data()
student3.display_data()

print('')
print(student1.get_email)
print(student2.get_email)
print(student3.get_email)

student2 = student1

print('')
print(student1.get_email)
print(student2.get_email)
print(student3.get_email)
