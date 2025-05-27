import json
from student import Student
from fees import Fees
from storage import Storage

def main():
    print("Welcome to the School Fees CLI")
    
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. View Students")
        print("3. Record Payment")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            record_payment()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def add_student():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    try:
        required_fees = float(input("Enter required fees: "))
    except ValueError:
        print("Invalid amount. Student not added.")
        return
    student = Student(name, student_id, required_fees)
    Storage.save_student(student)
    print(f"Student {name} added successfully.")

def view_students():
    students = Storage.load_students()
    if students:
        for student in students:
            remaining = student.required_fees - student.fees_paid
            status = "Fully Paid" if remaining <= 0 else f"Owes {remaining}"
            print(f"Name: {student.name}, ID: {student.student_id}, Paid: {student.fees_paid}, Required: {student.required_fees}, Status: {status}")
    else:
        print("No students found.")

def record_payment():
    student_id = input("Enter student ID: ")
    try:
        amount = float(input("Enter payment amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    fees_manager = Fees()
    if fees_manager.record_payment(student_id, amount):
        print("Payment recorded successfully.")
    else:
        print("Student not found.")

if __name__ == "__main__":
    main()