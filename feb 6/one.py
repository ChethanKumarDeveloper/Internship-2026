# Question 1: Write a Python program to find the factorial of a number using a loop

# Answer
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)

# Output
# Enter a number: 5
# Factorial = 120

#--------------

# Question 2: Write a Python program to print the multiplication table of a given number

# Answer
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Output
# Enter a number: 3
# 3 x 1 = 3
# ...
# 3 x 10 = 30

#--------------

# Question 3: Write a Python program to count the number of digits in a given number

# Answer
num = int(input("Enter a number: "))
count = 0

while num > 0:
    count += 1
    num //= 10

print("Number of digits =", count)

# Output
# Enter a number: 1234
# Number of digits = 4

#--------------

# Question 4: Write a Python program to reverse a number using a loop

# Answer
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

print("Reversed number =", rev)

# Output
# Enter a number: 123
# Reversed number = 321

#--------------

# Question 5: Write a Python program to check whether a number is a palindrome using loops

# Answer
num = int(input("Enter a number: "))
temp = num
rev = 0

while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

if num == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

# Output
# Enter a number: 121
# Palindrome

#--------------

# Question 6: Write a Python program to print numbers from 1 to 10 using a for loop

# Answer
for i in range(1, 11):
    print(i)

# Output
# 1
# 2
# ...
# 10

#--------------

# Question 7: Write a Python program to print numbers from 10 to 1 using a while loop

# Answer
i = 10

while i >= 1:
    print(i)
    i -= 1

# Output
# 10
# 9
# ...
# 1

#--------------

# Question 8: Write a Python program to generate the Fibonacci series up to N terms

# Answer
n = int(input("Enter number of terms: "))
a, b = 0, 1

for i in range(n):
    print(a)
    a, b = b, a + b

# Output
# Enter number of terms: 5
# 0
# 1
# 1
# 2
# 3

#--------------

# Question 9: Write a Python program to check whether a number is an Armstrong number using loops

# Answer
num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# Output
# Enter a number: 153
# Armstrong Number

#--------------

# Question 10: Write a Python program to find the sum of digits of a given number

# Answer
num = int(input("Enter a number: "))
sum = 0

while num > 0:
    sum += num % 10
    num //= 10

print("Sum of digits =", sum)

# Output
# Enter a number: 123
# Sum of digits = 6

#--------------

# Question 11: Write a Python program to print all prime numbers between 1 and 100

# Answer
for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

# Output
# 2
# 3
# 5
# ...
# 97

#--------------

# Question 12: Write a Python program to find the GCD of two numbers using a loop

# Answer
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD =", gcd)

# Output
# Enter first number: 12
# Enter second number: 18
# GCD = 6

#--------------

# Question 13: Write a Python program to find the LCM of two numbers using loops

# Answer
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

lcm = max(a, b)
while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1

print("LCM =", lcm)

# Output
# Enter first number: 4
# Enter second number: 6
# LCM = 12

#--------------

# Question 14: Write a Python program to print the following pattern using nested loops

# Answer
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Output
# *
# * *
# * * *
# * * * *
# * * * * *

#--------------

# Question 15: Write a Python program to print all even numbers between 1 and 50

# Answer
for i in range(2, 51, 2):
    print(i)

# Output
# 2
# 4
# ...
# 50

#--------------

# Question 16: Write a Python program to print all odd numbers between 1 and 100

# Answer
for i in range(1, 101, 2):
    print(i)

# Output
# 1
# 3
# ...
# 99

#--------------

# Question 17: Write a Python program to calculate the sum of first N natural numbers

# Answer
n = int(input("Enter N: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum =", sum)

# Output
# Enter N: 10
# Sum = 55
```
