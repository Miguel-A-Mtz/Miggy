# Miguel Martinez
# CIS 135 Summer Python Programming
# Lab 11: "Statement Nesting and Variable Scope"
# MIT Open Source License (License.html)

# Code Changes or Questions:
# What is the real placement of the period in mv_0 print string


def multiverse_0(visitor):
  # (scope return different var name
  name_visitor = visitor
  return name_visitor


def multiverse_1(visitor):
  new_string = visitor + " from Multiverse 1"
  return new_string


def multiverse_2(visitor):
  return "There is no escape from Multiverse 2"


def main():
  print("\nWelcome to lab 11 Multiverse Scope")



  # prompt user for name
  user_name = input("\n\tPlease enter a name: ")

  #  call multiverse(0)
  mv_0 = multiverse_0(user_name)
  print("\t\tData returned from multiverse_0 is({}): {}".format(user_name, mv_0))

  #  call multiverse(1)
  mv_1 = multiverse_1(user_name)
  print("\t\tData returned from multiverse_1 is({}): {}".format(user_name, mv_1))

  # call multiverse(2)
  mv_2 = multiverse_2(user_name)
  print("\t\tData returned from multiverse_2({}): {}".format(user_name, mv_2))

  # nested function calls
  print("\n\tStarting Nested Function Calls")
  multiverse_0(multiverse_1(user_name))
  print("\t\tNested call is: multiverse_0(multiverse_1({})): \n\t\t\tResult is: {}".format(user_name, multiverse_0(multiverse_1(user_name))))

  multiverse_0(multiverse_2(user_name))
  print("\t\tNested call is: multiverse_0(multiverse_2({})): \n\t\t\tResult is: {}".format(user_name, multiverse_0(multiverse_2(user_name))))

  multiverse_0(multiverse_1(multiverse_2(user_name)))
  print("\t\tNested call is: multiverse_0(multiverse_1(multiverse_2({}))): \n\t\t\tResult is: {}".format(user_name, multiverse_0(multiverse_1(multiverse_2(user_name)))))

  print("\nNow exiting lab 11")
  return


main()
