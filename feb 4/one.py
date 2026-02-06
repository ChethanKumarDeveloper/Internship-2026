# Question 1: Write a Python program to read two numbers and perform all arithmetic operations on them

# Answer
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)

# Output
# Enter first number: 10
# Enter second number: 5
# Addition = 15
# Subtraction = 5
# Multiplication = 50
# Division = 2.0

#--------------

# Question 2: Write a Python program to find the sum and average of three numbers

# Answer
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

sum = a + b + c
average = sum / 3

print("Sum =", sum)
print("Average =", average)

# Output
# Enter first number: 10
# Enter second number: 20
# Enter third number: 30
# Sum = 60
# Average = 20.0

#--------------

# Question 3: Write a Python program to find the area and perimeter of a rectangle

# Answer
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area =", area)
print("Perimeter =", perimeter)

# Output
# Enter length: 5
# Enter breadth: 3
# Area = 15
# Perimeter = 16

#--------------

# Question 4: Write a Python program to calculate simple interest

# Answer
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100
print("Simple Interest =", si)

# Output
# Enter principal: 1000
# Enter rate: 5
# Enter time: 2
# Simple Interest = 100.0

#--------------

# Question 5: Write a Python program to calculate the square and cube of a number

# Answer
num = int(input("Enter a number: "))

print("Square =", num ** 2)
print("Cube =", num ** 3)

# Output
# Enter a number: 4
# Square = 16
# Cube = 64

#--------------

# Question 6: Write a Python program to find the remainder and quotient of two numbers

# Answer
a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))

print("Quotient =", a // b)
print("Remainder =", a % b)

# Output
# Enter dividend: 17
# Enter divisor: 5
# Quotient = 3
# Remainder = 2

#--------------

# Question 7: Write a Python program to convert Celsius to Fahrenheit

# Answer
c = float(input("Enter temperature in Celsius: "))

f = (c * 9/5) + 32
print("Temperature in Fahrenheit =", f)

# Output
# Enter temperature in Celsius: 25
# Temperature in Fahrenheit = 77.0

#--------------

# Question 8: Write a Python program to calculate total marks, average, and percentage

# Answer
m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))

total = m1 + m2 + m3
average = total / 3
percentage = (total / 300) * 100

print("Total =", total)
print("Average =", average)
print("Percentage =", percentage)

# Output
# Enter marks 1: 80
# Enter marks 2: 70
# Enter marks 3: 90
# Total = 240
# Average = 80.0
# Percentage = 80.0

#--------------

# Question 9: Write a Python program to calculate the area of a circle

# Answer
radius = float(input("Enter radius: "))

area = 3.14 * radius * radius
print("Area of Circle =", area)

# Output
# Enter radius: 7
# Area of Circle = 153.86

#--------------

# Question 10: Write a Python program to find profit or loss

# Answer
cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if sp > cp:
    print("Profit =", sp - cp)
elif cp > sp:
    print("Loss =", cp - sp)
else:
    print("No Profit No Loss")

# Output
# Enter cost price: 100
# Enter selling price: 120
# Profit = 20
```
