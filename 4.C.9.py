Dict1={'Name':'Thanush','Age':19}
print("Dictionary 1 is",Dict1)
Dict2={'College':'GMR','Branch':'CSE'}
print("Dictionary 2 is",Dict2)
Dict=Dict1.update(Dict2)
print("Merging with update() keyword")
print(Dict1)

Dict1={'Name':'Thanush','Age':19}
Dict2={'College':'GMR','Branch':'CSE'}
Dict=Dict1|Dict2
print("Merging with '|' operator")
print(Dict)

#output
#Dictionary 1 is {'Name': 'Thanush', 'Age': 19}
#Dictionary 2 is {'College': 'GMR', 'Branch': 'CSE'}
#Merging with update() keyword
#{'Name': 'Thanush', 'Age': 19, 'College': 'GMR', 'Branch': 'CSE'}
#Merging with '|' operator
#{'Name': 'Thanush', 'Age': 19, 'College': 'GMR', 'Branch': 'CSE'}

