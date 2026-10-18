def make_counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print("Count =", count)

    return increment


counter = make_counter()

counter()
counter()
counter()
counter()

'''
Output:
Count = 1
Count = 2
Count = 3
Count = 4
'''
