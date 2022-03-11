# Author: Timur Guner
# Date: 2021-05-12
# Description: Project 6a takes of list of numbers and returns the max using recursion

def list_max(list, pos=0, max=0):
    """
    The list_max function takes in a list of numbers as the parameter. It then uses to recursion to return the maximum
    value in this list.
    """

    # If the recursion reaches the end of the list, we return the highest number in the list by using max as the index
    if pos == len(list)-1:
        return list[max]

    # If else statement is used to compare two numbers in the list and store the index of the max value until the
    # recursion is completer.
    if list[max] > list[pos + 1]:
        return list_max(list, pos+1, max)
    else:
        return list_max(list, pos+1, pos+1)