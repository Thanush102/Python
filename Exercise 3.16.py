n = int(input("Enter a number: "))
if n<1:
    print("enter positive numbers")
elif n==1:
    print("1 is prime aswell as not a prime")
elif n==2:
    print("2 is a prime")
else:  
    for i in range(2,n,1):
        if n%i==0:
            isprime=False
            break
        else:
            isprime=True
    if isprime == True:
        print(n,"is a prime")
    else:
        print(n,"is not a prime")

#OUTPUT
#Enter a number: 3
#3 is a prime

#Enter a number: 8
#8 is not a prime
