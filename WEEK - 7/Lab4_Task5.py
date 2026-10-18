items = {
    "Apple": 100,
    "Banana": 40,
    "Papaya": 60,
    "orange": 80
}

sorted_items = sorted(items.items(), key=lambda x: x[1])

print("Items sorted by price:")

for item in sorted_items:
    print(item[0], "-", item[1])

'''
Output:
Items sorted by price:
Banana - 40
Papaya - 60
orange - 80
Apple - 100
'''
