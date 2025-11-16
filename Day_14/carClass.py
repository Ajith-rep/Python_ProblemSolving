class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount
        return self.speed

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0   # prevent negative speed
        return self.speed

    def display(self):
        print(
            f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nSpeed: {self.speed}"
        )


car1 = Car("Mahindra", "BE 6", 2025, 90)
car1.accelerate(10)
car1.display()
car1.brake(50)
car1.display()
car1.brake(60)
car1.display()
