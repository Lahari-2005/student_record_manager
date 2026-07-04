import re

FILE_NAME = "students.txt"

# Function to validate email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

# Function to add student
def add_student():
    try:
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        email = input("Enter Email: ")

        if not validate_email(email):
            raise ValueError("Invalid Email Format!")

        with open(FILE_NAME, "a") as file:
            file.write(f"{student_id},{name},{age},{email}\n")

        print("Student record saved successfully.")

    except ValueError as e:
        print("Error:", e)

# Function to read student data
def read_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            if not data:
                print("No student records found.")
                return

            print("\nStudent Records")
            print("=" * 45)

            for record in data:
                student_id, name, age, email = record.strip().split(",")

                print(f"Student ID : {student_id}")
                print(f"Name       : {name}")
                print(f"Age        : {age}")
                print(f"Email      : {email}")
                print("_" * 45)

    except FileNotFoundError:
        print("Student data file not found.")

# Main Menu
while True:
    print("\n===== Student Record Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        read_students()

    elif choice == "3":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please try again.")
