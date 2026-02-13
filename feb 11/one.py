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



# Question 1: Write a Python program to create a list of integers and display it

# Answer
lst = [1, 2, 3, 4, 5]
print(lst)

# Output
# [1, 2, 3, 4, 5]

#--------------

# Question 2: Write a Python program to find the sum and average of elements in a list

# Answer
lst = [10, 20, 30]
sum_val = sum(lst)
avg = sum_val / len(lst)
print("Sum =", sum_val)
print("Average =", avg)

# Output
# Sum = 60
# Average = 20.0

#--------------

# Question 3: Write a Python program to find the largest and smallest element in a list

# Answer
lst = [5, 2, 9, 1]
print("Largest =", max(lst))
print("Smallest =", min(lst))

# Output
# Largest = 9
# Smallest = 1

#--------------

# Question 4: Write a Python program to count even and odd numbers in a list

# Answer
lst = [1, 2, 3, 4, 5]
even = odd = 0
for i in lst:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even =", even)
print("Odd =", odd)

# Output
# Even = 2
# Odd = 3

#--------------

# Question 5: Write a Python program to remove duplicate elements from a list

# Answer
lst = [1, 2, 2, 3, 4, 4]
new_list = list(set(lst))
print(new_list)

# Output
# [1, 2, 3, 4]

#--------------

# Question 6: Write a Python program to reverse a list

# Answer
lst = [1, 2, 3]
lst.reverse()
print(lst)

# Output
# [3, 2, 1]

#--------------

# Question 7: Write a Python program to sort elements of a list in ascending order

# Answer
lst = [4, 1, 3, 2]
lst.sort()
print(lst)

# Output
# [1, 2, 3, 4]

#--------------

# Question 8: Write a Python program to search for an element in a list

# Answer
lst = [10, 20, 30]
if 20 in lst:
    print("Element found")
else:
    print("Element not found")

# Output
# Element found

#--------------

# Question 9: Write a Python program to merge two lists

# Answer
list1 = [1, 2]
list2 = [3, 4]
merged = list1 + list2
print(merged)

# Output
# [1, 2, 3, 4]

#--------------

# Question 10: Write a Python program to find the second largest element in a list

# Answer
lst = [10, 40, 20, 30]
lst.sort()
print(lst[-2])

# Output
# 30

#--------------

# Question 11: Write a Python program to create a tuple and display its elements

# Answer
tpl = (1, 2, 3)
print(tpl)

# Output
# (1, 2, 3)

#--------------

# Question 12: Write a Python program to find the length of a tuple

# Answer
tpl = (5, 6, 7)
print(len(tpl))

# Output
# 3

#--------------

# Question 13: Write a Python program to find the maximum and minimum element in a tuple

# Answer
tpl = (8, 2, 5)
print("Max =", max(tpl))
print("Min =", min(tpl))

# Output
# Max = 8
# Min = 2

#--------------

# Question 14: Write a Python program to convert a tuple into a list

# Answer
tpl = (1, 2, 3)
lst = list(tpl)
print(lst)

# Output
# [1, 2, 3]

#--------------

# Question 15: Write a Python program to check whether an element exists in a tuple

# Answer
tpl = (10, 20, 30)
print(20 in tpl)

# Output
# True

