# Author: Timur Guner
# Date: 2021-05-12
# Description: Project 6b contains a function called is_decreasing and uses recursion to test if the list is strictly
#              decreasing in descending order

def is_decreasing(list, pos=0):
    """
    The is_decreasing function checks to see if the list of numbers in decreasing order
    """

    # If all numbers are in descending order when the last element in the list is checked, return True
    if pos == len(list)-1:
        return True

    # If the current number is greater than the second number, the use recursion to call the function incrementing pos
    # by one. Else, return False.
    if list[pos] > list[pos+1]:
        return is_decreasing(list, pos+1)
    else:
        return False
