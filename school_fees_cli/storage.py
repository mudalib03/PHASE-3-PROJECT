import json
import os
from student import Student

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "students.json")

class Storage:
    @staticmethod
    def load_students():
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
                return [Student.from_dict(item) for item in data]
            except json.JSONDecodeError:
                return []

    @staticmethod
    def save_students(students):
        with open(DATA_FILE, "w") as f:
            json.dump([s.to_dict() for s in students], f, indent=4)

    @staticmethod
    def save_student(student):
        students = Storage.load_students()
        # Prevent duplicate IDs
        for s in students:
            if s.student_id == student.student_id:
                print("Student ID already exists. Student not added.")
                return
        students.append(student)
        Storage.save_students(students)

    @staticmethod
    def update_student(student):
        students = Storage.load_students()
        for idx, s in enumerate(students):
            if s.student_id == student.student_id:
                students[idx] = student
                Storage.save_students(students)
                return True
        return False