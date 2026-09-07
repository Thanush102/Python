LIST = [2,4,66,3,2,44,3,5]
print("Original list",LIST)
list=[]
for i in LIST:
    if i not in list:
        list.append(i)
print("List after removing duplicates:",list)

#output
#Original list [2, 4, 66, 3, 2, 44, 3, 5]
#List after removing duplicates: [2, 4, 66, 3, 44, 5]
