a = int(input("enter lower limit"))
b = int(input("enter upper limit"))
count=0
if b<a:
    print("Since lower limit is greater than upper limit, swapped lower limit & upper limit")
    temp=a
    a=b
    b=temp
print(f"PRIME NUMBERS IN BETWEEN {a} and {b}:") 
for i in range(a,b+1):
    if i<2:
        continue
    isprime=True
    for j in range(2, int(i**0.5) + 1):
        if i%j==0:
            isprime=False
            break
    if isprime:
            print(i)
#OUTPUT
#enter lower limit3
#enter upper limit25
#PRIME NUMBERS IN BETWEEN 5 and 25:
#5
#7
#11
#13
#17
#19
#23
   
