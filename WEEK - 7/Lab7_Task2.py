def log_call(func):
    def wrapper(*args, **kwargs):
        print("Function is called")
        result = func(*args, **kwargs)
        print("Result:", result)
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b
add(9,5)

'''
Output:
Function is called
Result: 14
'''
