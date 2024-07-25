# Miguel Martinez
# CIS 135 Summer Python Programming
# Lab 4: Data types
# MIT Open Source License (License.html)

print("Welcome to lab 4 Data types")

# Create three variables
string_data = '20'
integer_data = 10
modify_data = 5.0
print(f'string_data is {string_data} and is type {type(string_data)}')
print(f'integer_data is {integer_data} and is type {type(integer_data)}')
print(f'modify_data is {modify_data} and is type {type(modify_data)}')

# Add string data to float data
# print("string_data {string_data} + modify_data {modify_data} = {modify_data + string_data}")

# Add int data to float data
print(f'{integer_data} + {modify_data} + {integer_data + modify_data}')

# Cast string to int, and add to float
int(string_data)
print(int(string_data))
print(f'{int(string_data)} is of type {type(int(string_data))}')
print(f'{int(string_data)} + {modify_data} = {int(string_data) + modify_data}')

# Prompt the user for an integer
user_number = int(input("please enter a number: "))
print(f'user_number is {user_number} and of type {type(user_number)}')
print(f'{user_number} + {modify_data} = {user_number + modify_data}')
