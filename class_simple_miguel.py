# Miguel Martinez
# CIS 135 Summer Python Programming
# Lab 18: Simple Class Declaration
# MIT Open Source License (License.html)

# Class Person
class Person:
    """ this is the type of comment we want
    :param - preferred_name (str)
    :param - life_goal (str)
    """
    # Data Members
    preferred_name = ""
    life_goal = ""

    def __init__(self,name, goal):
        """
        Initialize a Person object with preferred name and life goal data saved.
        param: preferred_name (str) - Preferred name of the person.
        param: life_goal (str) - Life goal of the person.
        self.preferred_name = name
        self.life_goal = goal
        """
        self.preferred_name = name
        self.life_goal = goal

    def describe_person(self):
        print("The goal of {} is to {}. ".format(self.preferred_name, self.life_goal))
        return

def main():

    # create a person object with name and goal
    me = Person("mehaq", "to be good")
    me_2 = Person("meho", "love good people")
    me.describe_person()
    me_2.describe_person()
    # print("The person {}, has the life goal {}".format(me.preferred_name, me.life_goal))

    return

main()