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



# Question 15: Write a Python function to find the largest element in a list

# Answer
def largest_element(lst):
    max_val = lst[0]
    for i in lst:
        if i > max_val:
            max_val = i
    return max_val

print(largest_element([10, 25, 7, 40, 18]))

# Output
# 40

#--------------

# Question 16: Write a Python function to count vowels in a string

# Answer
def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in 'aeiou':
            count += 1
    return count

print(count_vowels("education"))

# Output
# 5

#--------------

# Question 17: Write a Python function to check whether a string is a palindrome

# Answer
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))

# Output
# True

#--------------

# Question 18: Write a Python function to find the length of a string without using built-in functions

# Answer
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

print(string_length("Python"))

# Output
# 6

#--------------

# Question 19: Write a Python function to calculate the power of a number

# Answer
def power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

print(power(2, 5))

# Output
# 32

#--------------

# Question 20: Write a Python function to check whether a number is Armstrong

# Answer
def is_armstrong(num):
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10
    return total == num

print(is_armstrong(153))

# Output
# True

#--------------

# Question 21: Write a Python function to generate Fibonacci series up to n terms

# Answer
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(5)

# Output
# 0 1 1 2 3

#--------------

# Question 22: Write a Python function to calculate the average of numbers in a list

# Answer
def average(lst):
    total = 0
    for i in lst:
        total += i
    return total / len(lst)

print(average([10, 20, 30, 40]))

# Output
# 25.0

#--------------

# Question 23: Write a Python function to check whether a number is positive, negative, or zero

# Answer
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(-5))

# Output
# Negative

#--------------

# Question 24: Write a Python function to find the smallest number in a list

# Answer
def smallest_element(lst):
    min_val = lst[0]
    for i in lst:
        if i < min_val:
            min_val = i
    return min_val

print(smallest_element([8, 3, 15, 2, 9]))

# Output
# 2

#--------------

# Question 25: Write a Python function to count even and odd numbers in a list

# Answer
def count_even_odd(lst):
    even = odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

print(count_even_odd([1, 2, 3, 4, 5, 6]))

# Output
# (3, 3)

#--------------

# Question 26: Write a Python function to calculate the gross salary of an employee

# Answer
def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    return basic + hra + da

print(gross_salary(20000))

# Output
# 26000.0

#--------------

# Question 27: Write a Python function to find the GCD of two numbers

# Answer
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(12, 18))

# Output
# 6

#--------------

# Question 28: Write a Python function to find the LCM of two numbers

# Answer
def lcm(a, b):
    return (a * b) // gcd(a, b)

print(lcm(4, 6))

# Output
# 12

#--------------

# Question 29: Write a Python function to calculate the electricity bill using units consumed

# Answer
def electricity_bill(units):
    if units <= 100:
        return units * 1.5
    elif units <= 200:
        return (100 * 1.5) + (units - 100) * 2.5
    else:
        return (100 * 1.5) + (100 * 2.5) + (units - 200) * 4

print(electricity_bill(150))

# Output
# 275.0

#--------------

# Question 30: Write a Python function to display all prime numbers within a given range

# Answer
def primes_in_range(start, end):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num, end=" ")

primes_in_range(10, 30)

# Output
# 11 13 17 19 23 29



