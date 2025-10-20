details = {
    "Gopi" : 102444,
    "Shubh" : 999999,
    "Deep" : 1028,
    "Ram" : 1085,
    "Harman" : 1098
}
def deposit(withdraw, balance):
    if withdraw > balance:
        print("Insufficient Balance")
        return balance
    else:
        balance -= withdraw
        print("Withdrawal Successful")
        return balance
while True:
    print("Welcome to the ATM")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter your name: ")
        if name in details:
            print("Your balance is: ", details[name])
        else:
            print("Invalid Name")
    elif choice == 2:
        name = input("Enter your name: ")
        if name in details:
            withdraw = int(input("Enter the amount to withdraw: "))
            details[name] = deposit(withdraw, details[name])
            print(f"Your current balance is {details[name]}")
        else:
            print("Invalid Name")
    elif choice == 3:
        print("Thank you for using the ATM")
        break
    else:
        print("Invaild Choice")

# program is done