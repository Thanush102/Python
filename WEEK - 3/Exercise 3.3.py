
a=int(input("enter side a:"))
b=int(input("enter side b:"))
c=int(input("enter side c:"))

if((a+b)>c) and ((b+c)>a) and ((c+a)>b):
     if a==b and b==c:
         print("equilateral triangle")
     elif a==b or b==c or c==a:
         print("isosceles triangle")
     else :
         print("scalen triangle")

else :
     print("not a valid triangle")

#output
#enter side a:2
#enter side b:3
#enter side c:4
#scalen triangle
