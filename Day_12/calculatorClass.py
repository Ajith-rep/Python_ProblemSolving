class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print(f"Addition of the given numbers: {self.num1+self.num2}")        

    def sub(self):
        print(f"Subtraction of the given numbers: {self.num1-self.num2}")        

    def mul(self):
        print(f"Multiplication of the given numbers: {self.num1*self.num2}")        

    def div(self):
        print(f"Division of the given numbers: {self.num1/self.num2}")        

a = Calculator(15,6)
a.add()
a.sub()
a.mul()
a.div()