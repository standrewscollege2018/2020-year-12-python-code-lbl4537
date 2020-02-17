# manage student info about L1 NCEA credits
# Liam Blackmore
# 11/2/20

# Display name function
def display_all_students():
    for index in range(0, len(students)):
        print(index+1, students[index])


# stores student details
students = [["Lucas Very Cool",10], ["Danny B",0], ["Ollie Od",12], ["Rhys Brother", 65], ["Oooo Zac Moore", 112]]


# adding a student
student_name = input("Please enter a new student:")
student_credit_total = int(input("Enter total NCEA level 1 credits"))
new_student = [student_name, student_credit_total]

students.append(new_student)

# Display all students
display_all_students()

# Delete a student
student_num = int(input("Enter number of student to delete: "))
del(students[student_num-1])

# display all students in a list
display_all_students()

# change student details
student_num = int(input("What is the number of the student you wish to change? "))
new_name = input("Enter new name: ")
students[student_num-1] = (new_name)
new_total = int(input("Enter new credit total: "))  

# display all students
display_all_students()