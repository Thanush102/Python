LIST = [5,17,23,15,90,46,67]
print("Original list",LIST)
LIST.append(26)
print("List after append 26",LIST)
LIST.insert(4,45)
print("List after inserting 4 at 45 index",LIST)
LIST.extend([54])
print("List after extend element 54",LIST)
LIST.remove(46)
print("List after removing 46",LIST)
LIST.pop()
print("List after normal pop",LIST)
LIST.pop(5)
print("List after poping element atindex 5",LIST)
LIST.sort()
print("List after sort",LIST)
LIST.reverse()
print("Reverse of List",LIST)
print("No.of 2's in list:",LIST.count(2))
print("Element at index 5:",LIST.index(5))

#output
#Original list [5, 17, 23, 15, 90, 46, 67]
#List after append 26 [5, 17, 23, 15, 90, 46, 67, 26]
#List after inserting 4 at 45 index [5, 17, 23, 15, 45, 90, 46, 67, 26]
#List after extend element 54 [5, 17, 23, 15, 45, 90, 46, 67, 26, 54]
#List after removing 46 [5, 17, 23, 15, 45, 90, 67, 26, 54]
#List after normal pop [5, 17, 23, 15, 45, 90, 67, 26]
#List after poping element atindex 5 [5, 17, 23, 15, 45, 67, 26]
#List after sort [5, 15, 17, 23, 26, 45, 67]
#Reverse of List [67, 45, 26, 23, 17, 15, 5]
#No.of 2's in list: 0
#Element at index 5: 6
