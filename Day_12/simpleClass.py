class Student:
    def __init__(self,name,age,branch):
        self.name = name 
        self.age = age
        self.branch = branch
    def info(self):
        print(f" Name: {self.name}\n Age: {self.age} \n Branch: {self.branch}")

s1 = Student("Ajith",22,"CSE")
s1.info()
