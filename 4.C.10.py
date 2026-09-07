Items = {"pongal": 35, "Idli": 20, "vada": 25, "Poori": 25}
highest_item = max(Items, key=Items.get)
lowest_item = min(Items, key=Items.get)

print(f"Item with Highest Price is {highest_item} (Price: {Items[highest_item]})")
print(f"Item with Lowest Price is {lowest_item} (Price: {Items[lowest_item]})")

#output
#Item with Highest Price is pongal (Price: 35)
#Item with Lowest Price is Idli (Price: 20)


