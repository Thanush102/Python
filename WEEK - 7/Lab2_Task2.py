def  calculate_price(price, tax_rate=18, discount=0):
     tax = price * tax_rate / 100
     price = price + tax
     price = price - discount
     return price
print("(a) with only the price")
print(calculate_price(1000))
print("(b) with price and a custom tax_rate")
print(calculate_price(1000,10))
print(" (c) with all three arguments overridden")
print(calculate_price(1000,10,50))

'''
Output:
(a) with only the price
1180.0
(b) with price and a custom tax_rate
1100.0
 (c) with all three arguments overridden
1050.0
'''
