Set=set([0,1,99,5,9,7,12])
print(Set)
Set.remove(5)
print("Set after removig existing element 5:",Set)
Set.discard(77)
print("Set after removig non existing element 77:",Set)
Set.discard(7)
print("Set after removig existing element 7:",Set)

#output
#{0, 1, 99, 5, 7, 9, 12}
#Set after removig existing element 5: {0, 1, 99, 7, 9, 12}
#Set after removig non existing element 77: {0, 1, 99, 7, 9, 12}
#Set after removig existing element 7: {0, 1, 99, 9, 12}

