#This is a simple ATM simulator that validates a PIN and lets users check balance, withdraw, or deposit money.
amt=10000
pin=1234

print("Welcome to the ATM!")
entered_pin = int(input("Please enter your PIN: "))
if entered_pin == pin:
    print("PIN accepted. You can proceed with your transactions.")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    choice = int(input("Please select an option: "))
    
    if choice == 1:
        print(f"Your current balance is: ${amt}")
    elif choice == 2:
        withdraw_amount = int(input("Enter the amount to withdraw: "))
        if withdraw_amount <= amt:
            amt -= withdraw_amount
            print(f"You have withdrawn ${withdraw_amount}. Your new balance is: ${amt}")
        else:
            print("Insufficient funds.")
    elif choice == 3:
        deposit_amount = int(input("Enter the amount to deposit: "))
        amt += deposit_amount
        print(f"You have deposited ${deposit_amount}. Your new balance is: ${amt}")
    else:
        print("Invalid option selected.")


#output
# Welcome to the ATM!
# Please enter your PIN: 1234
# PIN accepted. You can proceed with your transactions.
# 1. Check Balance
# 2. Withdraw Money
# 3. Deposit Money
# Please select an option: 1
# Your current balance is: $10000

# Welcome to the ATM!
# Please enter your PIN: 1234
# PIN accepted. You can proceed with your transactions.
# 1. Check Balance
# 2. Withdraw Money
# 3. Deposit Money
# Please select an option: 2
# Enter the amount to withdraw: 3000
# You have withdrawn $3000. Your new balance is: $7000

# Welcome to the ATM!
# Please enter your PIN: 1234
# PIN accepted. You can proceed with your transactions.
# 1. Check Balance
# 2. Withdraw Money
# 3. Deposit Money
# Please select an option: 3
# Enter the amount to deposit: 1000000000000000
# You have deposited $1000000000000000. Your new balance is: $1000000000010000

def student_info(**data):
    print(data)
    for key, value in data.items():
        print(key,"=",value)

student_name = input("Enter student name: ")
student_age = input("Enter student age: ")
student_ph=input("Enter student phone number: ")
student_info(name=student_name, age=student_age, phone=student_ph)

#output
# Enter student name: Chethan
# Enter student age: 18
# Enter student phone number: 123456789
# {'name': 'Chethan', 'age': '18', 'phone': '123456789'}
# name = Chethan
# age = 18
# phone = 123456789


