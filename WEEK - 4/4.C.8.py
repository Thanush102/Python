Semlan={"1st Sem":"c","2nd Sem":"Data Structures","3rd Sem":"Python"}
print("Sem and Language:",Semlan)

key="1st Sem"
if key in Semlan:
    print(f"{key} is Found and value is {Semlan[key]}")
else:
    print(f"{key} is Not Found")

#OUTPUT
#Sem and Language: {'1st Sem': 'c', '2nd Sem': 'Data Structures', '3rd Sem': 'Python'}
#1st Sem is Found and value is c
    
