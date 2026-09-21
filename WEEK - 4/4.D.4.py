A = set((1,2,3,4))
print("Set A =",A)
B = set((3,4,5,6))
print("Set B =",B)

print("Union of A and B :",A.union(B))
print("Intersection of A and B :",A.intersection(B))
print("Difference of A and B :",A.difference(B))
print("Symmetric Difference of A and B :",A.symmetric_difference(B))

#output
#Set A = {1, 2, 3, 4}
#Set B = {3, 4, 5, 6}
#Union of A and B : {1, 2, 3, 4, 5, 6}
#Intersection of A and B : {3, 4}
#Difference of A and B : {1, 2}
#Symmetric Difference of A and B : {1, 2, 5, 6}
