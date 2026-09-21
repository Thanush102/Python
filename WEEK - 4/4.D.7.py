Set1=set([1,2,3])
print("Set1=",Set1)
Set2=set((4,5,6))
print("Set2=",Set2)
print("Set1 and Set2 are disjoint sets",Set1.isdisjoint(Set2))

"""
OUTPUT
Set1= {1, 2, 3}
Set2= {4, 5, 6}
Set1 and Set2 are disjoint sets True
"""
