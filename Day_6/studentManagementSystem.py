# Student Management System

students = []  # list to store all the student records


# function to add student
def add_student():
    student = {}
    student["id"] = int(input("Enter Student ID: "))
    student["name"] = input("Enter Student Name: ")
    student["age"] = input("Enter Age: ")
    student["course"] = input("Enter Course: ")
    student["marks"] = int(input("Enter Marks: "))
    students.append(student)
    print("Student Added Succesfully!")


# function to view all students
def view_student():
    if not students:
        print("No Students Found")
    else:
        print("Students List")
        for s in students:
            print(
                f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Course: {s['course']} | Marks: {s['marks']}"
            )


# function to search students
def search_student():
    sid = int(input("Enter Student ID to search: "))
    for s in students:
        if s["id"] == sid:
            print(
                f"\n Student Found:\n ID: {s['id']} |  Name: {s['name']} | Age: {s['age']} | Course: {s['course']} | Marks: {s['marks']}"
            )
            return
    print("Student Not Found!")


# function to update student details
def update_student():
    sid = int(input("Enter Student ID to update: "))
    for s in students:
        if s["id"] == sid:
            print(f"Updating record for {s['name']}")
            s["name"] = input("Enter new name: ")
            s["age"] = int(input("Enter new age: "))
            s["course"] = input("Enter new course: ")
            s["marks"] = float(input("Enter new marks: "))
            print("Student updated successfully!")
            return
    print("Student not found.")


# function to delete student details
def delete_student():
    sid = int(input("Enter Student ID to delete: "))
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Student deleted Succesfully!")
            return
    print("Student Not Found")


# Main Menu
def menu():
    while True:
        print("\n------ Student Management System ------")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = int(input("Enter the choice (1-6): "))

        if choice == 1:
            add_student()
        elif choice == 2:
            view_student()
        elif choice == 3:
            search_student()
        elif choice==4:
            update_student()
        elif choice==5:
            delete_student
        elif choice==6:
            break
        else:
            print("Invalid Choice, Try Again")

menu()