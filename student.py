
import os

FILE_NAME = "students.txt"

# ---------------- MENU ---------------- #
def show_menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")


# ---------------- VALIDATION ---------------- #
def is_valid_age(age):
    return age.isdigit() and 1 <= int(age) <= 120


# ---------------- ADD STUDENT ---------------- #
def add_student():
    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    grade = input("Enter Grade: ").strip()

    if not is_valid_age(age):
        print("Invalid age! Please enter a valid number.")
        return

    with open(FILE_NAME, "a") as file:
        file.write(f"{student_id},{name},{age},{grade}\n")

    print("✅ Student added successfully!")


# ---------------- VIEW STUDENTS ---------------- #
def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return

    with open(FILE_NAME, "r") as file:
        records = file.readlines()

    if not records:
        print("No student data available.")
        return

    print("\n--- Student Records ---")
    for record in records:
        student_id, name, age, grade = record.strip().split(",")
        print(f"ID: {student_id} | Name: {name} | Age: {age} | Grade: {grade}")


# ---------------- UPDATE STUDENT ---------------- #
def update_student():
    student_id = input("Enter Student ID to update: ").strip()

    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return

    updated = False
    new_records = []

    with open(FILE_NAME, "r") as file:
        records = file.readlines()

    for record in records:
        data = record.strip().split(",")
        if data[0] == student_id:
            print("Enter new details:")
            name = input("New Name: ").strip()
            age = input("New Age: ").strip()
            grade = input("New Grade: ").strip()

            if not is_valid_age(age):
                print("Invalid age! Update cancelled.")
                return

            new_records.append(f"{student_id},{name},{age},{grade}\n")
            updated = True
        else:
            new_records.append(record)

    if updated:
        with open(FILE_NAME, "w") as file:
            file.writelines(new_records)
        print("✅ Student record updated successfully!")
    else:
        print("Student ID not found.")


# ---------------- DELETE STUDENT ---------------- #
def delete_student():
    student_id = input("Enter Student ID to delete: ").strip()

    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return

    deleted = False
    new_records = []

    with open(FILE_NAME, "r") as file:
        records = file.readlines()

    for record in records:
        data = record.strip().split(",")
        if data[0] == student_id:
            deleted = True
        else:
            new_records.append(record)

    if deleted:
        with open(FILE_NAME, "w") as file:
            file.writelines(new_records)
        print("✅ Student deleted successfully!")
    else:
        print("Student ID not found.")


# ---------------- MAIN LOOP ---------------- #
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
