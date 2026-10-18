from functools import reduce
numbers = [2, 4, 6, 8]

# Product of numbers
product = reduce(lambda a, b: a * b, numbers)
print("Product:", product)

# Maximum value
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print("Maximum:", maximum)

# Join strings
words = ["Python", "is", "easy"]

sentence = reduce(lambda a, b: a + " " + b, words)
print("Sentence:", sentence)

'''
Output:Product: 384
Maximum: 8
Sentence: Python is easy
'''
