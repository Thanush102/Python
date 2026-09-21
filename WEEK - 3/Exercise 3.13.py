n = int(input("Enter the number: "))
i=1
if n<1:
    print("enter a positive number")
else:
    print("Multiplication table of",n)
    for i in range(1,11,1):
        print (n*i)


#OUTPUT
#Enter the number: 4
#Multiplication table of 4
#4
#8
#12
#16
#20
#24
#28
#32
#36
#40
