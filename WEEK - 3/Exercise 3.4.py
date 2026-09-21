
a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))
print("a =",a,"b =",b,"c =",c)

if a>b:
    if a>c:
        print("a is largest")

elif b>a:
    if b>c:
        print("b is largest")
        
elif c>a:
    if c>b:
        print("c is largest")


#output
#enter a:2
#enter b:6
#enter c:1
#a = 2 b = 6 c = 1
#b is largest

