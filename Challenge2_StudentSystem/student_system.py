def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    with open("students.txt", "a") as file:
        file.write(f"{name},{roll},{marks}\n")

    print("Student added successfully!\n")


def view_students():
    try:
        with open("students.txt", "r") as file:
            data = file.readlines()
            if not data:
                print("No records found.\n")
            else:
                print("\nStudent Records:")
                for line in data:
                    name, roll, marks = line.strip().split(",")
                    print(f"Name: {name}, Roll: {roll}, Marks: {marks}")
                print()
    except FileNotFoundError:
        print("No records found.\n")


while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Try again.\n")
