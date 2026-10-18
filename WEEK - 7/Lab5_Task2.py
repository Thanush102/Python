counter = 0

def increment_counter():
    global counter
    counter = counter + 1
    print("Counter =", counter)

increment_counter()
increment_counter()
increment_counter()
increment_counter()
increment_counter()

'''
Output:
Counter = 1
Counter = 2
Counter = 3
Counter = 4
Counter = 5
'''
