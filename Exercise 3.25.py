n=int(input("Enter n value : "))
for i in range(1, n + 1):
    
    for j in range(1, i + 1):
        print(j, end=" ")
        
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
        
    print()

#OUTPUT
#Enter n value : 4
#1 
#1 2 1 
#1 2 3 2 1 
#1 2 3 4 3 2 1 
