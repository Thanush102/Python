balance = 1000

def deposit(amount):
    global balance
    balance = balance + amount
    print("Amount deposited successfully")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance = balance - amount
        print("Amount withdrawn successfully")
    else:
        print("Insufficient balance")

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter amount: "))
        deposit(amount)

    elif choice == 2:
        amount = int(input("Enter amount: "))
        withdraw(amount)

    elif choice == 3:
        print("Balance =", balance)

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
        
'''
Output:
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 1
Enter amount: 26890
Amount deposited successfully

1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 2
Enter amount: 4567
Amount withdrawn successfully

1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 3
Balance = 23323

1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 4
Thank you!

'''
