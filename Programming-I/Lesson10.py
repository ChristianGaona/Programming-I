# Create a basic ATM system
balance = 1000

def deposit(quantity):  # Operation to deposit with 0.5% VAT
    global balance
    real_amount = quantity - (quantity * 0.005)
    balance += real_amount
    print(f"You have deposited ${real_amount}. Now your balance is ${balance}.")

def withdraw(quantity):  # Operation to withdraw with 0.7% VAT
    global balance
    if quantity <= balance:
        real_amount = quantity - (quantity * 0.007)
        balance -= real_amount
        print(f"You have withdraw ${real_amount}. Now your balance is ${balance}.")
    else:
        print("Insufficient balance to perform this operation.")

# User Interface
while True:
    print("Operations:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")

    option = input("Select an option: ")

    if option == '1':
        quantity = float(input("Enter the amount you want to deposit: "))
        deposit(quantity)
    elif option == '2':
        quantity = float(input("Enter the amount you want to withdraw: "))
        withdraw(quantity)
    elif option == '3':
        print("Thank you, come back soon.")
        break
    else:
        print("Non-existent operation, try again.")