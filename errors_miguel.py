# Miguel Martinez
# Introduction to Programming with Python
# Script 3: "Program Flow, Errors and Troubleshooting"
# MIT Open Source License (see license.html)

# 2a: get data
user_input = input("Please enter your name: ")
# 2b: compare data if an empty string is found
# if user_input == '':
if len(user_input) > 0:  # 2c (in valid)
    print("user input is valid, and is {}".format(user_input))
else:     # 3c print data
    print("user input is invalid, empty string found")
