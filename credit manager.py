# manage student info about L1 NCEA credits
# Liam Blackmore
# 11/2/20

# stores student details
students = ["Justine Lee", "Bryn Lewis", "Meredith Lewis", "Rhys Lewis"]

# adding a student
new_student = input("Please enter a new student:")
students.append(new_student)

# Delete a student
student_num = int(input("Enter number of student to delete: "))
del(students[student_num-1])

# display all students in a list
for index in range(0, len(students)):
    print(index+1, students[index])

# change student details
student_num = int(input("Enter number of student to change: "))
new_name
