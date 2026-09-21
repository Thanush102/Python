nested_tuple = (1, 2, [3, 4, 5])
print("Original tuple:", nested_tuple)
nested_tuple[2].append(8)
nested_tuple[2][0] = 90
print("Modified tuple:", nested_tuple)

#OUTPUT
#Original tuple: (1, 2, [3, 4, 5])
#Modified tuple: (1, 2, [90, 4, 5, 8])



