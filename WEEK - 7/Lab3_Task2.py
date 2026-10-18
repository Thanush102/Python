calls_to_5 = 0

def fibonacci(n):
    global calls_to_5

    if n == 5:
        calls_to_5 += 1

    if n <= 1:  # base cases
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

# Print the first 15 terms (n = 0 to 14)
print("First 15 Fibonacci terms:")
for i in range(15):
    print(fibonacci(i), end=" ")

# Count calls to fibonacci(5) while calculating fibonacci(10)
calls_to_5 = 0
fibonacci(10)
print(f"\n\nfibonacci(5) is called {calls_to_5} times while calculating fibonacci(10).")

"""
Output:First 15 Fibonacci terms:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 

fibonacci(5) is called 8 times while calculating fibonacci(10).
"""
