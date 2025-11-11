# Python decorators
def greet_dec(func):
    def wrap():
        print("Good Morning!")
        func()
        print("Have a nice day!")

    return wrap


@greet_dec
def name():
    print("My name is Ajith")


name()

# Can be used like this also
greet_dec(name)()
