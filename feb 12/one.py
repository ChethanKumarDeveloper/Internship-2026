# Activity: Temperature Logger
# Task:
# You have daily temperatures recorded:
# temps = [23, 25, 20, 19, 22, 24, 21]
# #### Write code to:
# Print the highest temperature
# Print the lowest temperature
# I
# # Print how many days are above 22°C
# # Add today's temperature to the list
temps = [23, 25, 20, 19, 22, 24, 21]
# # Print the highest temperature
highest_temp = max(temps)
print("Highest temperature:", highest_temp)
# # Print the lowest temperature
lowest_temp = min(temps)
print("Lowest temperature:", lowest_temp)
# # Print how many days are above 22°C
days_above_22 = sum(1 for temp in temps if temp > 22)
print("Number of days above 22°C:", days_above_22)
# # Add today's temperature to the list
todays_temp = 26  # Example temperature for today
temps.append(todays_temp)
print("Updated temperatures:", temps)

# #touple Activity: Student Grades
grades = (85, 92, 78, 96, 88)
print("Student Grades:", grades)
print("First grade:", grades[0])
print("Last grade:", grades[4])

s={1,2,3,4,5,"hello",2.3,"hi",2,3}
print(type(s))
print(len(s))
print(s)



# Question 16: Write a Python program to create a set and display its elements

# Answer
s = {1, 2, 3}
print(s)

# Output
# {1, 2, 3}

#--------------

# Question 17: Write a Python program to perform union, intersection, and difference on two sets

# Answer
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)
print(a & b)
print(a - b)

# Output
# {1, 2, 3, 4, 5}
# {3}
# {1, 2}

#--------------

# Question 18: Write a Python program to remove duplicate elements from a list using a set

# Answer
lst = [1, 2, 2, 3]
print(list(set(lst)))

# Output
# [1, 2, 3]

#--------------

# Question 19: Write a Python program to find the common elements between two sets

# Answer
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)

# Output
# {2, 3}

#--------------

# Question 20: Write a Python program to check whether one set is a subset of another

# Answer
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))

# Output
# True

#--------------

# Question 21: Write a Python program to create a dictionary of student details and display it

# Answer
student = {"name": "Ravi", "age": 20}
print(student)

# Output
# {'name': 'Ravi', 'age': 20}

#--------------

# Question 22: Write a Python program to add a new key-value pair to a dictionary

# Answer
student = {"name": "Ravi"}
student["marks"] = 85
print(student)

# Output
# {'name': 'Ravi', 'marks': 85}

#--------------

# Question 23: Write a Python program to delete a key from a dictionary

# Answer
student = {"name": "Ravi", "age": 20}
del student["age"]
print(student)

# Output
# {'name': 'Ravi'}

#--------------

# Question 24: Write a Python program to search for a key in a dictionary

# Answer
student = {"name": "Ravi"}
print("name" in student)

# Output
# True

#--------------

# Question 25: Write a Python program to find the sum of all values in a dictionary

# Answer
d = {'a': 10, 'b': 20}
print(sum(d.values()))

# Output
# 30

#--------------

# Question 26: Write a Python program to count the frequency of each element in a list using dictionary

# Answer
lst = [1, 2, 2, 3]
freq = {}
for i in lst:
    freq[i] = freq.get(i, 0) + 1
print(freq)

# Output
# {1: 1, 2: 2, 3: 1}

#--------------

# Question 27: Write a Python program to merge two dictionaries

# Answer
d1 = {'a': 1}
d2 = {'b': 2}
d1.update(d2)
print(d1)

# Output
# {'a': 1, 'b': 2}

#--------------

# Question 28: Write a Python program to print keys and values of a dictionary separately

# Answer
d = {'x': 10, 'y': 20}
print(d.keys())
print(d.values())

# Output
# dict_keys(['x', 'y'])
# dict_values([10, 20])

#--------------

# Question 29: Write a Python program to find the maximum and minimum value in a dictionary

# Answer
d = {'a': 10, 'b': 5}
print(max(d.values()))
print(min(d.values()))

# Output
# 10
# 5

#--------------

# Question 30: Write a Python program to sort a dictionary by its keys

# Answer
d = {'b': 2, 'a': 1}
sorted_d = dict(sorted(d.items()))
print(sorted_d)

# Output
# {'a': 1, 'b': 2}


