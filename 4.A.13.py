LIST=[23,24,26,12,45,65,3,46,67,1,456,0,1234]
max=sum=min=0
n=len(LIST)
for i in range(n):
    if LIST[i]>max:
        max=LIST[i]
    if LIST[i]<min:
        min=LIST[i]
    sum+=LIST[i]
print(LIST)
print(f"Maximum number is {max},Minimum number is {min},Sum of all is {sum}")

#output
#[23, 24, 26, 12, 45, 65, 3, 46, 67, 1, 456, 0, 1234]
#Maximum number is 1234,Minimum number is 0,Sum of all is 2002
