def smart_divide(func):
    def wrapper(a, b):
        if b == 0:
            print("Cannot divide by zero!")
            return
        return func(a, b)

    return wrapper


@smart_divide
def divide(a, b):
    print(a / b)


divide(5,2)
divide(10,0)