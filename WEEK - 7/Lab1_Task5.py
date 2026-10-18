def celsius_to_fahrenheit(c):
    return(c*9/5)+32
def fahrenheit_to_celsius(f):
    return(f-32)*5/9
while True:
    print("\n1.Celsius to Farenheit:")
    print("\n2.Farenheit to Celsius:")
    print("\n3.Exit")
    choice = int(input("Enter your choice:"))

    if choice==1:
        c=float(input("Enter the celsius value:"))
        print(celsius_to_fahrenheit(c))
    elif choice==2:
        f=float(input("Enter the fahrenheit value:"))
        print(fahrenheit_to_celsius(f))
    elif choice==3:
        print("Exiting")
        break
    else :
        print("invalid choice")

'''
Output:
1.Celsius to Farenheit:

2.Farenheit to Celsius:

3.Exit
Enter your choice:1
Enter the celsius value:23
73.4

1.Celsius to Farenheit:

2.Farenheit to Celsius:

3.Exit
Enter your choice:2
Enter the fahrenheit value:56.9
13.833333333333334

1.Celsius to Farenheit:

2.Farenheit to Celsius:

3.Exit
Enter your choice:3
Exiting







