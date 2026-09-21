n=int(input("Enter n value:"))
num = 1
for i in range(n+1):
    for j in range(i):
        print(num, end=" ")
        num+=1
    print()

#OUTPUT
#Enter n value:4

#1 
#2 3 
#4 5 6 
#7 8 9 10 
