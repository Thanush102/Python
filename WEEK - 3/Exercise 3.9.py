n = int(input("Enter a number: "))
sum=0
if n==0:
    print("Sum is 0 and Average is 0")
else:
    while n!=0:
        digit=n%10
        n=n//10
        sum+=digit

    print("Sum is",sum)
    print("Average is",sum/3)

#OUTPUT
#Enter a number: 56
#Sum is 11
#Average is 3.6666666666666665
