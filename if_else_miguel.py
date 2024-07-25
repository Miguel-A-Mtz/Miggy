# Miguel Martinez
# CIS 135 Summer Python Programming
# Lab 5: If, Elif, Else (comparisons)
# MIT Open Source License (License.html)

print("Welcome to lab 5 Comparing data")

year = 2024
user_data = int(input("please enter a year as four digits i.e., 2024:"))
print(f"You entered {user_data}, which is of type {type(user_data)}")

# Evaluate user data
if user_data == year:  # exactly equal
    print(f"Your data is the same as the current year {year}")
elif user_data < year:  # less than <
    print(f"Your data {user_data} is less than the current year {year}")
else:  # elif user_data > year:
    print(f"Your data {user_data} is greater than the current year {year}")
    