# Miguel Martinez
# Introduction to programming with python
# Script 7: "while loops, using counter variables"
# MIT Open Source License (see License.html)

print("\nWelcome to Lab 7 on while loops)")

# #Loop 1: Check counter for less than or equal to max
counter, my_max, my_min = 0, 10, 1
while counter < my_max:
    print("counter is less than max: counter = {}".format(counter))
    counter += 1


# Loop 2
print("\nCounting down from 10")
while counter >= my_min:
    counter -= 1
    print("\tCounter is greater than min : counter = {}".format(counter))

# Loop 3
user_counter = 0
user_input = 1
sum_total = 0
print("\nUser Input Counter:")
while user_input >= 0:
    user_input = int(input("\tEnter a negative number to exit"))
    user_counter += 1  # user_counter = user_counter + 1
    sum_total += user_input
print("\t\tuser_counter value is {}".format(user_counter))
print("\t\tsum_total value is {}".format(sum_total))

# user_input, user_counter = 1, 0
# user_input = input()


print("\nThank you")
