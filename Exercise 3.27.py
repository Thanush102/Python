n=int(input("Enter n value:"))
print("* "*n)
s=n-2
for i in range(1,n-1):
    space=" "*(2*s)
    star="* "
    print(star+space+star)
print("* "*n)

#OUTPUT
#Enter n value:4
#* * * * 
#*     * 
#*     * 
#* * * * 

