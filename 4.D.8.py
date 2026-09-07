List=[0,1,7,3,8,45,18,33,9,27,6,12,64,99,83,45,7,18,3,8]
print("Original List is :",List)
List=set(List)
print("Unique List(set):",List)
List=sorted(List)
print("Unique List(sorted):",List)

#output
#Original List is : [0, 1, 7, 3, 8, 45, 18, 33, 9, 27, 6, 12, 64, 99, 83, 45, 7, 18, 3, 8]
#Unique List(set): {0, 1, 33, 3, 64, 99, 6, 7, 8, 9, 12, 45, 18, 83, 27}
#Unique List(sorted): [0, 1, 3, 6, 7, 8, 9, 12, 18, 27, 33, 45, 64, 83, 99]
