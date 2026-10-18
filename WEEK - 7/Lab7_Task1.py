def greet():
    print("Hello, Python!")

# 1. Assign function to another variable
a = greet
a()

# 2. Pass function as an argument
def call_function(func):
    func()
call_function(greet)

# 3. Return a function from another function
def outer():
    def inner():
        print("This is an inner function")
    return inner
b = outer()
b()

'''
Output:
Hello, Python!
Hello, Python!
This is an inner function
'''
