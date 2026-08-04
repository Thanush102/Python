
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(list1 == list2) 
print(list1 is list2)  
print(list1 is list3) 
print(id(list1), id(list2), id(list3))

#output
#True
#False
#True
#2439856320384 2439856311360 2439856320384
