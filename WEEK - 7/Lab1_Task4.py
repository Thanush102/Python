def stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers)/len(numbers)
    return minimum, maximum,average
numbers = [10,15,25,48,59,64,100]
minimum, maximum, average = stats(numbers)
print("Numbers:", numbers)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)

'''
Output:
Numbers: [10, 15, 25, 48, 59, 64, 100]
Minimum: 10
Maximum: 100
Average: 45.857142857142854
'''
