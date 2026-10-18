def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

# Convert Celsius to Fahrenheit
temperatures = [0, 25, 30, 40]
result = list(map(celsius_to_fahrenheit, temperatures))
print("Fahrenheit:", result)

# Convert strings to uppercase
words = ["hello", "python", "java", "programming"]
result = list(map(str.upper, words))
print("Uppercase:", result)

'''
Output:
Fahrenheit: [32.0, 77.0, 86.0, 104.0]
Uppercase: ['HELLO', 'PYTHON', 'JAVA', 'PROGRAMMING']
'''
