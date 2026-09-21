LIST1=[12,34,23,57,78,34,95,10]
LIST2=[11,3,33,67]
print("List1:",LIST1)
print("List2:",LIST2)
for item in LIST2:
    LIST1.append(item)
LIST1.sort()
print("Merged list after sorting:",LIST1)

#OUTPUT
#List1: [12, 34, 23, 57, 78, 34, 95, 10]
#List2: [11, 3, 33, 67]
#Merged list after sorting: [3, 10, 11, 12, 23, 33, 34, 34, 57, 67, 78, 95]
