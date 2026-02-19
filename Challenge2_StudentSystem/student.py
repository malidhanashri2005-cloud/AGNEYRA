# Challenge2_StudentSystem/student.py

import os

STUDENTS_FILE = "Challenge2_StudentSystem/students.txt"

def load_students():
    students = []
    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    name, age, grade = line.split(",")
                    students.append({"name": name, "age": age, "grade": grade})
    return students

def save_students(students):
    with open(STUDENTS_FILE, "w") as f:
        for s in students:
            f.write(f"{s['name']},{s['age']},{s['grade']}\n")

def add_student(students):
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    students.append({"name": name, "age": age, "grade": grade})
    save_students(students)
    print(f"{name} added successfully!")

def view_students(students):
    if not students:
        print("No students found.")
        return
    print("\n--- Student List ---")
    for i, s in enumerate(students, start=1):
        print(f"{i}. Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}")
    print("-------------------\n")

def main():
    students = load_students()
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            print("Exiting Student System. Bye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
