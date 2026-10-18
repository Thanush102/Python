def repeat(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator
@repeat(3)
def greet():
    print("Hello! Welcome to Python.")
greet()

'''
Output:
Hello! Welcome to Python.
Hello! Welcome to Python.
Hello! Welcome to Python.
'''
