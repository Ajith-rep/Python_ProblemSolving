class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        count = 0
        for _ in self.marks:
            count += 1
        average = sum(self.marks) / count
        return average

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def display(self):
        print(f"Name: {self.name}\nAverage: {self.average()}\nGrade: {self.grade()}")


stud1 = Student("Ajith", [90, 80, 70])
stud1.display()

