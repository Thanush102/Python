import time
def log_call(func):
    def wrapper():
        print("Function is called")
        result = func()
        print("Function returned:", result)
        return result
    return wrapper

def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print("Execution time:", end - start, "seconds")
        return result
    return wrapper
@log_call
@timer
def calculate_sum():
    total = 0
    for i in range(100000):
        total = total + i
    return total

calculate_sum()

'''
Output:
Function is called
Execution time: 0.00356292724609375 seconds
Function returned: 4999950000
'''
