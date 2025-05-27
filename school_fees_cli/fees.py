from storage import Storage

class Fees:

    def record_payment(self, student_id, amount):
        students = Storage.load_students()
        for student in students:
            if student.student_id == student_id:
                student.fees_paid += amount
                Storage.update_student(student)
                return True
        return False