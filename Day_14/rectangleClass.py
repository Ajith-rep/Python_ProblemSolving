class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(f"Area of rectangle: {self.length * self.breadth}")

    def peri(self):
        print(f"Perimeter of rectangle: {2*(self.length+self.breadth)}")


parameters1 = Rectangle(5,5)
parameters1.area()
parameters1.peri()