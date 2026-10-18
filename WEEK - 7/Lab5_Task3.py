counter = 0

def change_counter():
    global counter
    counter = counter + 1
    print("Counter =", counter)

change_counter()

'''
Output:
Counter = 1
'''
