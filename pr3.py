students = []

print("\nvery very Welcome to the Student Management System!")

while True:
    print("\nPlease select option sir:")
    print("1. Add student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        stdId = input("Student ID: ")  
        stdName = input("Name: ")
        stdAge = input("Age: ")
        stdGrade = input("Grade: ")
        stdDOB = input("Date of Birth (YYYY-MM-DD): ")
        stdSubjects = input("Subjects (comma-separated): ")

        new_student = {
            "id": stdId,
            "name": stdName,
            "age": stdAge,
            "grade": stdGrade,
            "dob": stdDOB,
            "subjects": stdSubjects
        }
        students.append(new_student)
        print("Student added by SMS successfully!")

    elif choice == "2":
        if not students:
            print("No student found by SMS.")
        else:
            print("-------- Students List --------")
            for student in students:
                print("ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, "
                      "Grade: {student['grade']}, DOB: {student['dob']}, Subjects: {student['subjects']}")

    elif choice == "3":
        uId = input("Enter Student ID to update: ")  
        found = False
        for student in students:
            if student["id"] == uId:
                uName = input("Enter new name : ")
                uAge = input("Enter new age : ")
                uGrade = input("Enter new grade : ")
                uDOB = input("Enter new DOB : ")

                if uName:
                    student["name"] = uName
                if uAge:
                    student["age"] = uAge
                if uGrade:
                    student["grade"] = uGrade
                if uDOB:
                    student["dob"] = uDOB

                print("Student updated successfully by SMS !")
                found = True
                break
        if not found:
            print("No student found with that ID.")

    elif choice == "4":
        dId = input("Enter Student ID to delete: ")  
        found = False
        for student in students:
            if student["id"] == dId:
                students.remove(student)
                print("Student deleted successfully by SMS!")
                found = True
                break
        if not found:
            print("No student found with that ID.")

    elif choice == "5":
        if not students:
            print("No students available by SMS.")
        else:
            print("Subjects offered by all students:")
            for student in students:
                print("{student['name']} → {student['subjects']}")

    elif choice == "6":
        print("Thanks for using the Student Management System!")
        break

    else:
        print("sorry sir, please try again.")

'''
very very Welcome to the Student Management System!

Please select option sir:
1. Add student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 1
Student ID: 1
Name: krishna V
Age: 17
Grade: A1
Date of Birth (YYYY-MM-DD): 16-3-2008
Subjects (comma-separated): design
Student added by SMS successfully!

Please select option sir:
1. Add student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 1
Student ID: 2
Name: dinesh
Age: 18
Grade: A+++++++++++++++
Date of Birth (YYYY-MM-DD): 1-6-2007
Subjects (comma-separated): coderio
Student added by SMS successfully!

Please select option sir:
1. Add student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 3
Enter Student ID to update: 1
Enter new name : krish
Enter new age : 17
Enter new grade : A-____
Enter new DOB : 129-219
Student updated successfully by SMS !

Please select option sir:
1. Add student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 4
Enter Student ID to delete: 1
Student deleted successfully by SMS!

Please select option sir:
1. Add student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 2
-------- Students List --------
ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, DOB: {student['dob']}, Subjects: {student['subjects']}

Please select option sir:
1. Add student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 2
-------- Students List --------
ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, DOB: {student['dob']}, Subjects: {student['subjects']}

Please select option sir:
1. Add student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 1
Student ID: 1
Name: krish
Age: gs
Grade: gsd
Date of Birth (YYYY-MM-DD): gd
Subjects (comma-separated): ghd
Student added by SMS successfully!

Please select option sir:
1. Add student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 2
-------- Students List --------
ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, DOB: {student['dob']}, Subjects: {student['subjects']}
ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, DOB: {student['dob']}, Subjects: {student['subjects']}

Please select option sir:
1. Add student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 4
Enter Student ID to delete: 2,1
No student found with that ID.

Please select option sir:
1. Add student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 5
Subjects offered by all students:
{student['name']} → {student['subjects']}
{student['name']} → {student['subjects']}

Please select option sir:
1. Add student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 6
Thanks for using the Student Management System!

'''
