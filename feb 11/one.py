# #write the code to understand def function in python
# from unittest import result


def greet(name):
    print("Hello, " + name + ". Good morning!")
greet("Chethan")
greet("Suresh")
greet("Ramesh")

a=input(int("Enter a number: "))
b=input(int("Enter another number: "))
def add(a,b):
    return a+b  

sum = add(a,b)
print("The sum is:", result)

#Find the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
number = int(input("Enter a number: "))
result = factorial(number)
print("The factorial of", number, "is", result)

#Write code to get otp using random module
import random
def generate_otp(length):
    digits = "0123456789"
    otp = ""
    for _ in range(length):
        otp += random.choice(digits)
    return otp
otp_length = 6
otp = generate_otp(otp_length)
print("Your OTP is:", otp)

#Write code to get float otp using random module
import random
def generate_float_otp(length):
    digits = "0123456789"
    otp = ""
    for _ in range(length):
        otp += random.choice(digits)
    return float(otp)
float_otp_length = 6
float_otp = generate_float_otp(float_otp_length)
print("Your float OTP is:", float_otp)

#write code to add 2 numbers using add function
def add(a,b):
    return a+b
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("The sum is:", add(num1,num2))

