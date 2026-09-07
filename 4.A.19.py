LIST = [2,45,7,18,-3,-12,49,-1,-0]
print("Original List:",LIST)
List = [0 if item<=0 else item for item in LIST]
print(List)


#OUTPUT
#Original List: [2, 45, 7, 18, -3, -12, 49, -1, 0]
#[2, 45, 7, 18, 0, 0, 49, 0, 0]

