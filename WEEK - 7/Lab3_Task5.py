def gcd(a, b):
    if b == 0:  # base case
        return (a)
    return gcd(b, a % b)

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return (a * b) // gcd(a, b)

print("GCD:", gcd(6, 0))  
print("LCM:", lcm(39, 60)) 

"""
Output:
GCD: 6
LCM: 780
"""
