import time as t


def timer(func):
    def wrapper(*args, **kwargs):
        start = t.time()
        result = func(*args, **kwargs)
        end = t.time()
        print(f"{func.__name__} took {end - start:.4f} seconds to execute")
        return result

    return wrapper


@timer
def greet():
    print("Good Morning")


greet()
print()

@timer
def sum(n):
    total = 0
    for i in range(n):
        total += i
    return total


print(sum(5))
