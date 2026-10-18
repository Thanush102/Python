def order_summary(customer, *items, discount=0, **extra):
    print("Customer:", customer)
    print("Items:")
    for item in items:
        print(item)

    print("Discount:", discount, "%")

    print("Extra Information:")
    for key, value in extra.items():
        print(key, ":", value)

order_summary(
    "Thanush",
    "Laptop",
    "Mouse",
    discount=10,
    delivery_address="Rajam",
    gift_wrap=True
)
