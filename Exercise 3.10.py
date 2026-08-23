n = int(input("Enter a number: "))
rev = 0
if n>=0 and n<10:
    print("reverse is",n)
else:
    while n!=0:
        digit=n%10
        n=n//10
        rev = (rev*10)+digit

    print("reverse is",rev)

#OUTPUT
#Enter a number: 456789
#reverse is 987654

