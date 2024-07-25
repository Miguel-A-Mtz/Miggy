# Miguel Martinez
# CIS 135 Summer Python Programming
# Lab 6: Multiple Evaluation

print("Welcome to lab 6 AND and OR")

# my_min = 0
# my_max = 256
my_min, my_max = 0, 256
user_data = int(input("Please enter and number from 0 - 255: "))

# Use a compound AND evaluation
# that checks int(data) is greater than or equal to min
# AND less than max.
# Print the result.

# if user_data <= my_min and user_data < my_max:
if my_min <= user_data < my_max:
    print(f"{user_data} is greater than or equal to {my_min} and less than {my_max}")
elif user_data < my_min or user_data >= my_max:
    print(f'{user_data} is less than {my_min} or greater than or equal to {my_max}')

# OR evaluation that checks int(data) is less than min OR greater than or equal to max. Print the result.
