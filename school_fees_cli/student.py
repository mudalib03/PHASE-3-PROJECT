class Student:
    def __init__(self, name, student_id, required_fees, fees_paid=0.0):
        self.name = name
        self.student_id = student_id
        self.required_fees = required_fees
        self.fees_paid = fees_paid

    def to_dict(self):
        return {
            "name": self.name,
            "student_id": self.student_id,
            "required_fees": self.required_fees,
            "fees_paid": self.fees_paid
        }

   @staticmethod
    def from_dict(data):
        return Student(
            data["name"],
            data["student_id"],
            data["required_fees"],
            data.get("fees_paid", 0.0)
        )