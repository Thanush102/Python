Tuple = (15,23,86,67,92)
print("Tuple",Tuple)
key = int(input("Enter a value:"))
found=0
for item in Tuple:
    if item==key:
        found+=1
        break
if found==1:
    print("Value exists in Tuple")
else:
    print("Value is not exists in Tuple")

#OUTPUT
#Tuple (15, 23, 86, 67, 92)
#Enter a value:23
#Value exists in Tuple
