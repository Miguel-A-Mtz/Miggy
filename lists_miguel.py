# Miguel Martinez
# CIS 135 Summer Python Programming
# Lab 12: "Arrays (List, Tuples and Sets);"
# MIT Open Source License (License.html)

def main():
    print("\"Welcome to lab 12 Lists")

    binary_numbers = (1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111)
    one_to_ten = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine" "ten")

    print("\n\tThe value of binary_numbers is : {}".format(binary_numbers))
    print("\tThe value of one_to_ten is : {}".format(one_to_ten))

    # third, fifth, and seventh value(s)
    print("\n\tThe value of binary_numbers[2] or the third position  : {}".format(binary_numbers[2]))
    print("\tThe value of binary_numbers[4] or the fifth position   :{}".format(binary_numbers[4]))
    print("\tThe value of binary_numbers[6] or the seventh position   :{}".format(binary_numbers[6]))

    print("\n\tThe value of one_to_ten[2] or the third position   :{}".format(one_to_ten[2]))
    print("\tThe value of one_to_ten[4] or the fifth position   :{}".format(one_to_ten[4]))
    print("\tThe value of one_to_ten[6] or the seventh position   :{}".format(one_to_ten[6]))

    # For each tuple print out the fourth, fifth, sixth, seventh and eighth value(s)
    print("\n\tThe value of positions 4 - 8 or indexes 3-7: {}".format(binary_numbers[3:7]))
    # For either of the tuples, unpack (and print) the zeroth and last value(s)
    zero, last = one_to_ten[0], one_to_ten[-1]
    print("\n\tThe zeroth of one_to_ten[0]: {}, and last piece data one_to_ten[-1] is {}".format(zero, last))


    print("\nList component of lab 12:")
    # Component on Lists
    one_to_twelve = list()
    # loop, using range, add values zero through(including) ten
    for each in range(0, 11):
     one_to_twelve.append(each)
    print("\n\tThe value of one_to_twelve are {}".format(one_to_twelve))

    # insert(11) append(12) syntax to add values for 11 and 12
    one_to_twelve.insert(len(one_to_twelve) + 1, 11)
    print("\tInserted 11 at -1 position {}".format(one_to_twelve))
    one_to_twelve.append(12)
    print("\tAppended 12 at and  {}".format(one_to_twelve))


    #array.pop() syntax to remove the value (0) in the zeroth position.
    one_to_twelve.pop(0)
    print("\tPopped the zero at index-0 {}".format(one_to_twelve))

    # Print the values of the list in ascending and descending order.
    print("\tList in ascending order {}".format(one_to_twelve))
    reversed_list = list()
    for value in reversed(one_to_twelve):
        reversed_list.append(value)
    print("\tList in decending order {}.".format(reversed_list))

    print("\nNow exiting lab 12")
    return


main()
