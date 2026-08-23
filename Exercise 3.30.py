n=int(input("Enter n value:"))
star='*'
space=' '
for i in range(n,0,-1):
    print(star*(n-i+1)+space*(2*(i-1))+star*(n-i+1))
for i in range(1,n+1):
    print(star*(n-i+1)+space*(2*(i-1))+star*(n-i+1))

#OUTPUT
#Enter n value:5
#*        *
#**      **
#***    ***
#****  ****
#**********
#**********
#****  ****
#***    ***
#**      **
#*        *
