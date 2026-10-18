def simple_intrest(principal,time,intrest):
    return (principal * time * intrest)/100
p=float(input("Enter the principal amount:"))
t=float(input("Enter the time period:"))
r=float(input("Enter the rate of intrest:"))
print(f"Simple Intrest is {simple_intrest(p,t,r)}")

'''
output:
Enter the principal amount:100000
Enter the time period:5
Enter the rate of intrest:1.8
Simple Intrest is 9000.0
'''
