class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def apply_bonus(self, bonus):
        self.salary += self.salary * (bonus / 100)

    def apply_tax(self, tax):
        self.salary -= self.salary * (tax / 100)

    def annual_salary(self):
        return self.salary * 12

    def display(self):
        print(
            f"Name: {self.name}\nPosition: {self.position}\nCurrent Salary: {self.salary} \nAnnual Salary: {self.annual_salary()}"
        )


emp1 = Employee("Ajith", 40000, "Dev")
emp1.apply_bonus(10)
emp1.display()
