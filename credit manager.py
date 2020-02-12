# manage student info about L1 NCEA credits
# Liam Blackmore
# 11/2/20

# Display name function
def display_all_students():
    for index in range(0, len(students)):
        print(index+1, students[index])


# stores student details
students = ["Lucas Very Cool", "Danny B", "Ollie Od", "Rhys Brother", "Oooo Zac Moore"]

# adding a student
new_student = input("Please enter a new student:")
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

# display all students
display_all_students()