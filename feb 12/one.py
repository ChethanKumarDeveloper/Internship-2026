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
