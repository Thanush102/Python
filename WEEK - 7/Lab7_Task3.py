import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution time:", end - start, "seconds")
    return wrapper

@timer
def calculate_sum():
    total = 0
    for i in range(1000000):
        total = total + i
    print("Sum:", total)

calculate_sum()

'''
Output:
Sum: 499999500000
Execution time: 0.05043959617614746 seconds
'''
