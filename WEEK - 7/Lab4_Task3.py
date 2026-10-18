students = [("Thanush", 78), ("Kushal", 92), ("Nani", 65)]

# Sort students by marks
students.sort(key=lambda s: s[1], reverse=True)
print("Students sorted by marks:")
print(students)

# Sort words by length
words = ["apple", "kiwi", "banana", "cat"]
words.sort(key=lambda x: len(x))
print("Words sorted by length:")
print(words)

'''
Output:
Students sorted by marks:
[('Kushal', 92), ('Thanush', 78), ('Nani', 65)]
Words sorted by length:
['cat', 'kiwi', 'apple', 'banana']
'''
