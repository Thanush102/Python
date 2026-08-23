n = int(input("Enter a number : "))
rev = 0
temp=n
if n>=0 and n<10:
    print(n,"is a palindrome")
else:
    while temp!=0:
        digit = temp%10
        temp=temp//10
        rev=(rev*10)+digit
    print("Reverse is",rev)
    if rev==n:
        print(n,"is a palindrome")
    else:
        print(n,"is not apalindrome")

#OUTPUT
#Enter a number : 2344
#Reverse is 4432
#2344 is not apalindrome

#Enter a number : 12321
#Reverse is 12321
#12321 is a palindrome

    
