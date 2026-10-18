from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Using filter, map and reduce
even = filter(lambda x:x%2==0,numbers)
squares = map(lambda x:x**2,even)
total = reduce(lambda a,b:a+b,squares)
print("Total using reduce:",total)

# Using list comprehension and sum
total = sum([x**2 for x in numbers if x%2==0])
print("Total using sum:", total)

'''
Output:
Total using reduce: 220
Total using sum: 220
'''
