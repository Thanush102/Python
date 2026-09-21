n = int(input("Enter n value: "))
i=1
a=0
b=1
fib=1
if n<=0:
    print("Invalid input, enter positive numbers only")
else:
    print("Fibnocci Series")
    if n==1:
        print(a,b)
    else:
        print(a)
        while i<n:
            print(b)
            a, b = b, a + b
            i+=1

#OUTPUT
#Enter n value: 7
#Fibnocci Series
#0
#1
#1
#2
#3
#5
#8
